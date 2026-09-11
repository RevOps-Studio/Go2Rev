import fs from 'node:fs/promises';
import path from 'node:path';
// Fuente editable del producto: reglas generales y campos de entrada vacíos.
export async function construirModelo({Workbook, SpreadsheetFile, output, previews}) {
await fs.mkdir(output, { recursive: true });
await fs.mkdir(previews, { recursive: true });
const wb = Workbook.create();
const names = ['Economia', 'Umbrales', 'Capacidad', 'Caja', 'Existencias', 'Recurrencia'];
const sheets = Object.fromEntries(names.map(n => [n, wb.worksheets.add(n)]));
const ink = '#17212B', navy = '#17324D', pale = '#EEF3F7', inputFill = '#FFF2CC';
const numeric = '#,##0.00;[Red](#,##0.00);"—"';
const nc = '"No calculable"';
const blankInputs = [];
function cell(s,a,v) { s.getRange(a).values=[[v]]; }
function formula(s,a,f) { s.getRange(a).formulas=[[f]]; s.getRange(a).format.font.color=f.includes("'!")?'#008000':'#000000'; }
function input(s,a,fmt) {
  s.getRange(a).format.fill=inputFill;
  s.getRange(a).format.font.color='#0000FF';
  if(fmt) s.getRange(a).setNumberFormat(fmt);
  blankInputs.push([s.name,a]);
}
function list(s,a,values) { s.getRange(a).dataValidation={rule:{type:'list',values}}; }
function band(s,a,title) {
  s.getRange(a).format.fill=navy;
  s.getRange(a).format.font={name:'Arial',size:10,bold:true,color:'#FFFFFF'};
  cell(s,a.split(':')[0],title);
}
function header(s,a,labels) {
  const r=s.getRange(a); r.values=[labels];
  r.format.fill=navy; r.format.font={name:'Arial',size:10,bold:true,color:'#FFFFFF'};
  r.format.wrapText=true; r.format.horizontalAlignment='center'; r.format.rowHeight=42;
}
function setup(s,title,lastCol,lastRow) {
  s.showGridLines=false;
  const area=s.getRange(`C2:${lastCol}${lastRow}`);
  area.format.font={name:'Arial',size:10,color:ink};
  area.format.verticalAlignment='center'; area.format.rowHeight=28;
  area.format.columnWidth=16; area.setNumberFormat(numeric);
  s.getRange('A:B').format.columnWidth=2.5;
  s.getRange(`C2:C${lastRow}`).format.columnWidth=32;
  s.getRange(`C2:${lastCol}3`).format.fill=navy;
  s.getRange(`C2:${lastCol}3`).format.font={name:'Arial',size:14,color:'#FFFFFF',bold:true};
  cell(s,'C2',title);
  s.getRange(`C3:${lastCol}3`).format.font={name:'Arial',size:10,color:'#D9E2EA'};
  cell(s,'C3','Go2Rev · Modelo general v0.1 · Entradas vacías');
  s.freezePanes.freezeRows(3);
}
function warn(s,a) {
  s.getRange(a).conditionalFormats.add('containsText',{text:'Revisar',format:{fill:'#FCE8E6',font:{color:'#B42318',bold:true}}});
  s.getRange(a).conditionalFormats.add('containsText',{text:'No calculable',format:{fill:'#FFF2CC',font:{color:'#8A4B08'}}});
}
function link(s,a,target) { formula(s,a,`=IF(${target}="","",${target})`); }
function total(s,dest,range,rows,extra='TRUE') {
  formula(s,dest,`=IF(AND(COUNT(${range})>0,COUNT(${range})=COUNTA(${rows}),${extra}),SUM(${range}),${nc})`);
}

// Núcleo económico: cantidades reconocidas, costes variables y fijos pertinentes.
const e=sheets.Economia;
setup(e,'Economía de la combinación','N',56); e.tabColor=navy;
const meta=[['C5','Combinación y revisión','E5'],['G5','Moneda y escala','J5'],['C6','Periodo reconocido','E6'],['G6','Base e impuestos','J6'],['C7','Cobertura del perímetro','E7'],['G7','AF / contrato K12','J7']];
for(const [a,l,b] of meta) {cell(e,a,l);input(e,b);}
list(e,'E7',['Completa','Parcial']); e.getRange('E5:F7').format.wrapText=true;
e.getRange('J5:N7').format.wrapText=true;
header(e,'C10:E10',['Magnitud','Valor','Unidad']);
const resultLabels=['Ingreso del periodo','Contribución del periodo','Fijos pertinentes','Resultado del perímetro','Margen de contribución'];
resultLabels.forEach((l,i)=>cell(e,`C${11+i}`,l));
for(let r=11;r<=14;r++)link(e,`E${r}`,'$J$5'); cell(e,'E15','Proporción');
const ecoScope='AND($E$5<>"",$E$6<>"",$J$5<>"",$J$6<>"",$J$7<>"")';
total(e,'D11','J26:J37','C26:C37',`AND(${ecoScope},COUNTIFS(N26:N37,"Revisar identificación")=0)`);
total(e,'D12','K26:K37','C26:C37',`AND(${ecoScope},COUNTIFS(N26:N37,"Revisar identificación")=0)`);
total(e,'D13','I44:I51','C44:C51',`AND(${ecoScope},COUNTIFS(I44:I51,"No calculable")=0)`);
formula(e,'D14',`=IF(AND(COUNT(D12:D13)=2,E7="Completa"),D12-D13,${nc})`);
formula(e,'D15',`=IF(AND(COUNT(D11:D12)=2,D11>0),D12/D11,${nc})`);
e.getRange('D15').setNumberFormat('0.0%');
cell(e,'G10','Lectura del cálculo');
cell(e,'G11','Resultado del perímetro definido en K12.');
cell(e,'G12','Contribución después de variables comerciales.');
cell(e,'G13','Cantidad reconocida puede diferir de entrega y cobro.');
cell(e,'G14','Completar el alcance antes de interpretar sostenibilidad.');
cell(e,'C18','Amarillo: entrada editable. No calculable: falta dato, dominio o cobertura.');
cell(e,'C19','Un cero requiere fuente. Referencias AF por cada entrada material en la fila.');
cell(e,'C21','Separar costes del periodo de asignaciones unitarias para no sumarlos dos veces.');
header(e,'C25:N25',['Oferta / ID único','Unidad reconocida','Cantidad','Ingreso neto / unidad','Variable entrega / unidad','Variable comercial / unidad','Contribución / unidad','Ingreso','Contribución total','Cobertura variable','AF por entrada','Estado de fila']);
input(e,'C26:H37');input(e,'L26:M37');list(e,'L26:L37',['Completa','Parcial']);
e.getRange('M26:N37').format.wrapText=true; e.getRange('M25:N37').format.columnWidth=24;
for(let r=26;r<=37;r++) {
  const id=`AND(C${r}<>"",D${r}<>"",COUNTIFS($C$26:$C$37,C${r})=1,M${r}<>"")`;
  formula(e,`I${r}`,`=IF(COUNTA(C${r}:H${r},L${r}:M${r})=0,"",IF(AND(${id},COUNT(F${r}:H${r})=3,MIN(F${r}:H${r})>=0,L${r}="Completa"),F${r}-SUM(G${r}:H${r}),${nc}))`);
  formula(e,`J${r}`,`=IF(COUNTA(C${r}:H${r},L${r}:M${r})=0,"",IF(AND(${id},COUNT(E${r}:F${r})=2,MIN(E${r}:F${r})>=0),E${r}*F${r},${nc}))`);
  formula(e,`K${r}`,`=IF(COUNTA(C${r}:H${r},L${r}:M${r})=0,"",IF(AND(ISNUMBER(E${r}),E${r}>=0,ISNUMBER(I${r})),E${r}*I${r},${nc}))`);
  formula(e,`N${r}`,`=IF(COUNTA(C${r}:H${r},L${r}:M${r})=0,"",IF(NOT(${id}),"Revisar identificación",IF(AND(ISNUMBER(J${r}),ISNUMBER(K${r})),"Calculable","Revisar entradas")))`);
}
header(e,'C43:I43',['Partida fija / ID único','Importe del periodo','Clasificación / rango','AF / revisión / campo','Inclusión una sola vez','Cobertura','Importe admitido']);
input(e,'C44:H51');list(e,'G44:G51',['Incluida aquí']);list(e,'H44:H51',['Completa','Parcial']);
e.getRange('E44:H51').format.wrapText=true;
for(let r=44;r<=51;r++)formula(e,`I${r}`,`=IF(COUNTA(C${r}:H${r})=0,"",IF(AND(C${r}<>"",COUNTIFS($C$44:$C$51,C${r})=1,ISNUMBER(D${r}),D${r}>=0,E${r}<>"",F${r}<>"",G${r}="Incluida aquí",H${r}="Completa"),D${r},${nc}))`);
cell(e,'C53','Si no existen fijos pertinentes, documentar una partida de importe cero y su fundamento.');
cell(e,'C54','Lotes, escalones y ajustes requieren descomposición y dominio en K12.');
warn(e,'D11:D15'); warn(e,'N26:N37');

// Bloque algebraico de precio y equilibrio para una unidad homogénea.
const u=sheets.Umbrales;
setup(u,'Precio y equilibrio en un rango estable','H',31);
cell(u,'C5','Unidad / rango / revisión');input(u,'D5');cell(u,'F5','Alcance definido en K12');
cell(u,'C6','Combinación');link(u,'D6',"'Economia'!E5");
header(u,'C7:G7',['Parámetro','Valor','AF / campo / revisión','Unidad','Dominio']);
const drivers=[
 ['Coste unitario sin porcentaje','M / unidad','No negativo'],['Coste proporcional al precio','Proporción','Desde 0 hasta menos de 1'],['Fijos pertinentes','M / periodo','No negativo'],['Cantidad objetivo','Unidades / periodo','Positiva'],['Resultado objetivo','M / periodo','No negativo'],['Precio neto considerado','M / unidad','No negativo'],['Precio de lista','M / unidad','Positivo'],['Unidad indivisible','Condición','Sí o No'],['Cobertura y rango estable','Condición','Completa o Parcial']
];
drivers.forEach((d,i)=>{const r=i+8;cell(u,`C${r}`,d[0]);cell(u,`F${r}`,d[1]);cell(u,`G${r}`,d[2]);});
input(u,'D8:E16');u.getRange('D9').setNumberFormat('0.0%');list(u,'D15',['Sí','No']);list(u,'D16',['Completa','Parcial']);
u.getRange('E7:E16').format.columnWidth=30;u.getRange('G7:G16').format.columnWidth=28;
u.getRange('C7:G16').format.wrapText=true;
header(u,'C19:E19',['Relación','Resultado','Significado']);
const base='AND(D5<>"",D6<>"",D16="Completa",E16<>"")';
formula(u,'D20',`=IF(AND(${base},COUNTBLANK(E8:E12)=0,COUNT(D8:D12)=5,MIN(D8:D10)>=0,D9<1,D11>0,D12>=0),(D8+(D10+D12)/D11)/(1-D9),${nc})`);
formula(u,'D21',`=IF(AND(${base},E8<>"",E9<>"",COUNT(D8:D9)=2,D8>=0,D9>=0,D9<1,ISNUMBER(D13),D13>=0,E13<>""),D13*(1-D9)-D8,${nc})`);
formula(u,'D22',`=IF(AND(ISNUMBER(D21),ISNUMBER(D10),D10>=0,E10<>"",E15<>"",OR(D15="Sí",D15="No")),IF(D21>0,IF(D15="Sí",ROUNDUP(D10/D21,0),D10/D21),IF(AND(D21=0,D10=0),"Resultado cero en el rango","Sin equilibrio positivo")),${nc})`);
formula(u,'D23',`=IF(AND(ISNUMBER(D20),ISNUMBER(D14),D14>0,E14<>""),1-D20/D14,${nc})`);
u.getRange('D23').setNumberFormat('0.0%');
['Precio para cubrir objetivo','Contribución al precio considerado','Cantidad de equilibrio','Descuento máximo sobre lista'].forEach((l,i)=>cell(u,`C${20+i}`,l));
['No acredita aceptación comercial','Coste proporcional incluido una vez','Sujeto a capacidad y rango','Negativo: lista insuficiente'].forEach((l,i)=>cell(u,`E${20+i}`,l));
u.getRange('C20:E23').format.wrapText=true;u.getRange('D20:D23').format.columnWidth=27;u.getRange('C20:E23').format.rowHeight=38;
cell(u,'C26','Bloque independiente para una unidad. Cada parámetro referencia K12 y la configuración.');
cell(u,'C27','No aplica equilibrio simple a mezcla cambiante, lotes o escalones sin resolverlos.');
cell(u,'C28','Una fórmula calculable no adopta precio ni autoriza descuento.');warn(u,'D20:D23');

// Capacidad: tareas por recurso con conversión desde la unidad reconocida.
const c=sheets.Capacidad;
setup(c,'Carga por recurso y mezcla','N',62);
cell(c,'C5','Combinación');link(c,'E5',"'Economia'!E5");cell(c,'G5','Periodo');link(c,'I5',"'Economia'!E6");
cell(c,'C6','Cobertura de recursos');input(c,'E6');list(c,'E6',['Completa','Parcial']);
cell(c,'G6','Incluye todos los recursos indispensables y tareas pertinentes.');
cell(c,'C8','Factibilidad agregada');
formula(c,'E8',`=IF(AND(E5<>"",I5<>""),IF(COUNTIFS(I14:I21,"<0")>0,"Incompatible con recurso conocido",IF(AND(E6="Completa",COUNTA(C14:C21)>0,COUNT(I14:I21)=COUNTA(C14:C21),COUNTIFS(N14:N21,"Revisar identificación")=0,COUNTIFS(K27:K58,"Revisar entradas")=0),"Cabe en el periodo modelado",${nc})),${nc})`);
cell(c,'C9','Factor de escala de la mezcla');
formula(c,'E9',`=IF(AND(E8="Cabe en el periodo modelado",COUNT(J14:J21)>0),MIN(J14:J21),${nc})`);
cell(c,'G9','Solo carga lineal y preparación fija; no resuelve agenda ni demanda.');
c.getRange('E8:F9').format.wrapText=true;c.getRange('E8:E9').format.columnWidth=28;c.getRange('C8:N9').format.rowHeight=38;
header(c,'C13:N13',['Recurso / ID único','Disponible total','Otros compromisos','Carga propia fija','Carga variable','Carga total propia','Holgura','Factor de escala','Unidad recurso','AF / revisión','Cobertura recurso','Estado de fila']);
input(c,'C14:F21');input(c,'K14:M21');list(c,'M14:M21',['Completa','Parcial']);
c.getRange('L13:N21').format.columnWidth=24;c.getRange('L14:N21').format.wrapText=true;
header(c,'C26:K26',['Recurso / ID','Oferta / ID','Cantidad reconocida','Conversión a unidad de trabajo','Recurso por unidad de trabajo','Carga','AF por entrada / transformación','Cobertura tarea','Estado de fila']);
input(c,'C27:D58');input(c,'F27:G58');input(c,'I27:J58');list(c,'J27:J58',['Completa','Parcial']);
c.getRange('I26:K58').format.columnWidth=23;c.getRange('I27:K58').format.wrapText=true;
for(let r=27;r<=58;r++) {
  const active=`COUNTA(C${r}:D${r},F${r}:G${r},I${r}:J${r})`;
  const ids=`AND(C${r}<>"",D${r}<>"",COUNTIFS($C$14:$C$21,C${r})=1,COUNTIFS('Economia'!$C$26:$C$37,D${r})=1)`;
  const quantity=`INDEX('Economia'!$E$26:$E$37,MATCH(D${r},'Economia'!$C$26:$C$37,0))`;
  formula(c,`E${r}`,`=IF(${active}=0,"",IF(${ids},IF(${quantity}="",${nc},IF(ISNUMBER(${quantity}),${quantity},${nc})),${nc}))`);
  formula(c,`H${r}`,`=IF(${active}=0,"",IF(AND(COUNT(E${r}:G${r})=3,MIN(E${r}:G${r})>=0,I${r}<>"",J${r}="Completa"),PRODUCT(E${r}:G${r}),${nc}))`);
  formula(c,`K${r}`,`=IF(${active}=0,"",IF(AND(${ids},ISNUMBER(H${r})),"Calculable","Revisar entradas"))`);
}
for(let r=14;r<=21;r++) {
  const active=`COUNTA(C${r}:F${r},K${r}:M${r})`;
  const ids=`AND(C${r}<>"",COUNTIFS($C$14:$C$21,C${r})=1,K${r}<>"",L${r}<>"")`;
  const complete=`AND(${ids},M${r}="Completa",COUNTIFS($C$27:$C$58,C${r})=COUNTIFS($C$27:$C$58,C${r},$K$27:$K$58,"Calculable"))`;
  formula(c,`G${r}`,`=IF(${active}=0,"",IF(${complete},SUMIFS($H$27:$H$58,$C$27:$C$58,C${r}),${nc}))`);
  formula(c,`H${r}`,`=IF(${active}=0,"",IF(AND(ISNUMBER(F${r}),F${r}>=0,ISNUMBER(G${r})),F${r}+G${r},${nc}))`);
  formula(c,`I${r}`,`=IF(${active}=0,"",IF(AND(COUNT(D${r}:E${r})=2,MIN(D${r}:E${r})>=0,ISNUMBER(H${r})),D${r}-E${r}-H${r},${nc}))`);
  formula(c,`J${r}`,`=IF(${active}=0,"",IF(AND(ISNUMBER(I${r}),ISNUMBER(G${r})),IF(G${r}>0,(D${r}-E${r}-F${r})/G${r},"Sin carga variable"),${nc}))`);
  formula(c,`N${r}`,`=IF(${active}=0,"",IF(NOT(${ids}),"Revisar identificación",IF(ISNUMBER(I${r}),"Calculable","Revisar entradas")))`);
}
cell(c,'C60','Cobertura completa sin tareas variables declara carga variable cero; fundamentar en AF.');
cell(c,'C61','La conversión y preparación deben incorporar entrega, venta, soporte y lote pertinentes.');warn(c,'E8:E9');warn(c,'K27:K58');warn(c,'N14:N21');
c.getRange('I14:I21').conditionalFormats.add('cellIs',{operator:'lessThan',formula:0,format:{fill:'#FCE8E6',font:{color:'#B42318'}}});

// Caja por eventos contiguos, fechados y ordenados; no imputación automática desde resultado.
const ca=sheets.Caja;
setup(ca,'Caja por eventos','M',51);
for(const [a,l,b] of [['C5','Inicio del horizonte','E5'],['C6','Fin del horizonte','E6'],['C7','Saldo inicial disponible','E7'],['G5','Reserva mínima','I5'],['G6','Cobertura de obligaciones','I6'],['G7','AF / condiciones / moneda','I7']]){cell(ca,a,l);input(ca,b);}
ca.getRange('E5:E6').setNumberFormat('dd/mm/yy');list(ca,'I6',['Completa','Parcial']);
cell(ca,'C9','Saldo mínimo, incluido inicio');cell(ca,'C10','Financiación adicional necesaria');cell(ca,'C11','Saldo al final de eventos');
const cashScope='AND(COUNT(E5:E7)=3,E6>=E5,I6="Completa",I7<>"",COUNTA(C16:C47)>0,COUNT(I16:I47)=COUNTA(C16:C47),COUNTIFS(L16:L47,"Revisar entradas")=0)';
formula(ca,'E9',`=IF(${cashScope},MIN(E7,I16:I47),${nc})`);
formula(ca,'E10',`=IF(AND(ISNUMBER(E9),ISNUMBER(I5),I5>=0),MAX(0,I5-E9),${nc})`);
formula(ca,'E11',`=IF(${cashScope},E7+SUM(H16:H47),${nc})`);
cell(ca,'G10','La brecha no acredita financiación disponible.');
header(ca,'C15:M15',['Evento / ID único','Fecha','Orden en fecha','Cobro','Pago','Flujo neto','Saldo tras evento','AF / importe y fecha','Condición / obligación','Estado de fila','Clasificación']);
input(ca,'C16:G47');input(ca,'J16:K47');input(ca,'M16:M47');ca.getRange('D16:D47').setNumberFormat('dd/mm/yy');ca.getRange('E16:E47').setNumberFormat('0');
ca.getRange('J15:M47').format.columnWidth=25;ca.getRange('J16:M47').format.wrapText=true;
for(let r=16;r<=47;r++) {
  const active=`COUNTA(C${r}:G${r},J${r}:K${r},M${r})`;
  const order=r===16?'TRUE':`AND(C${r-1}<>"",ISNUMBER(D${r-1}),ISNUMBER(E${r-1}),OR(D${r}>D${r-1},AND(D${r}=D${r-1},E${r}>E${r-1})))`;
  const valid=`AND(C${r}<>"",COUNTIFS($C$16:$C$47,C${r})=1,COUNT(D${r}:G${r})=4,COUNT($E$5:$E$6)=2,$E$6>=$E$5,D${r}>=$E$5,D${r}<=$E$6,E${r}>0,E${r}=INT(E${r}),MIN(F${r}:G${r})>=0,J${r}<>"",K${r}<>"",M${r}<>"",${order})`;
  formula(ca,`H${r}`,`=IF(${active}=0,"",IF(${valid},F${r}-G${r},${nc}))`);
  const prev=r===16?'$E$7':`I${r-1}`;
  formula(ca,`I${r}`,`=IF(${active}=0,"",IF(AND(ISNUMBER(H${r}),ISNUMBER(${prev})),${prev}+H${r},${nc}))`);
  formula(ca,`L${r}`,`=IF(${active}=0,"",IF(ISNUMBER(I${r}),"Calculable","Revisar entradas"))`);
}
cell(ca,'C49','Completar filas contiguas en orden de fecha y secuencia; incluir ceros conocidos de cobro/pago.');
cell(ca,'C50','No compensar eventos si su orden afecta a financiación. Un evento incompleto limita saldos posteriores.');warn(ca,'E9:E11');warn(ca,'L16:L47');

// Relaciones auxiliares: no se agregan unidades distintas ni se duplican ingresos.
const st=sheets.Existencias;
setup(st,'Existencias utilizables','M',29);
cell(st,'C5','Corte inicial');input(st,'E5','dd/mm/yy');cell(st,'G5','Corte final');input(st,'I5','dd/mm/yy');
cell(st,'C7','Por artículo, unidad y ubicación. El saldo final no comprueba disponibilidad intraperiodo.');
header(st,'C10:M10',['Artículo / ubicación','Unidad','Stock inicial','Recepciones útiles','Devoluciones útiles','Salidas','Pérdidas','Stock final','AF por entrada','Cobertura','Estado de fila']);
input(st,'C11:I26');input(st,'K11:L26');list(st,'L11:L26',['Completa','Parcial']);st.getRange('K10:M26').format.columnWidth=25;st.getRange('K11:M26').format.wrapText=true;
for(let r=11;r<=26;r++) {
  const active=`COUNTA(C${r}:I${r},K${r}:L${r})`;
  const valid=`AND(C${r}<>"",D${r}<>"",COUNTIFS($C$11:$C$26,C${r},$D$11:$D$26,D${r})=1,COUNT(E${r}:I${r})=5,MIN(E${r}:I${r})>=0,K${r}<>"",L${r}="Completa",COUNT($E$5,$I$5)=2,$I$5>=$E$5)`;
  formula(st,`J${r}`,`=IF(${active}=0,"",IF(${valid},SUM(E${r}:G${r})-SUM(H${r}:I${r}),${nc}))`);
  formula(st,`M${r}`,`=IF(${active}=0,"",IF(ISNUMBER(J${r}),IF(J${r}<0,"Stock incompatible","Calculable"),"Revisar entradas"))`);
}
cell(st,'C28','Compras, consumo, valoración, reconocimiento y pago requieren sus relaciones en K11/K12.');warn(st,'M11:M26');
st.getRange('J11:J26').conditionalFormats.add('cellIs',{operator:'lessThan',formula:0,format:{fill:'#FCE8E6',font:{color:'#B42318'}}});
const re=sheets.Recurrencia;
setup(re,'Base activa y exposición','P',30);
cell(re,'C5','Inicio del periodo');input(re,'E5','dd/mm/yy');cell(re,'H5','Fin del periodo');input(re,'J5','dd/mm/yy');
cell(re,'C7','Exposición según fechas y contrato. No se infiere facturación de la media de clientes.');
header(re,'C10:P10',['Cohorte / oferta','Unidad de exposición','Base inicial','Altas','Bajas','Base final','Exposición reconocida','Precio / exposición','Ingreso','Variable / exposición','Contribución','AF por entrada','Cobertura','Estado de fila']);
input(re,'C11:G26');input(re,'I11:J26');input(re,'L11:L26');input(re,'N11:O26');list(re,'O11:O26',['Completa','Parcial']);
re.getRange('N10:P26').format.columnWidth=25;re.getRange('N11:P26').format.wrapText=true;
for(let r=11;r<=26;r++) {
  const active=`COUNTA(C${r}:G${r},I${r}:J${r},L${r},N${r}:O${r})`;
  const id=`AND(C${r}<>"",D${r}<>"",COUNTIFS($C$11:$C$26,C${r})=1,N${r}<>"",COUNT($E$5,$J$5)=2,$J$5>=$E$5)`;
  formula(re,`H${r}`,`=IF(${active}=0,"",IF(AND(${id},COUNT(E${r}:G${r})=3,MIN(E${r}:G${r})>=0,G${r}<=E${r}+F${r}),SUM(E${r}:F${r})-G${r},${nc}))`);
  formula(re,`K${r}`,`=IF(${active}=0,"",IF(AND(${id},ISNUMBER(H${r}),COUNT(I${r}:J${r})=2,MIN(I${r}:J${r})>=0),I${r}*J${r},${nc}))`);
  formula(re,`M${r}`,`=IF(${active}=0,"",IF(AND(ISNUMBER(K${r}),ISNUMBER(L${r}),L${r}>=0,O${r}="Completa"),K${r}-I${r}*L${r},${nc}))`);
  formula(re,`P${r}`,`=IF(${active}=0,"",IF(AND(ISNUMBER(H${r}),ISNUMBER(K${r}),ISNUMBER(M${r})),"Calculable","Revisar entradas"))`);
}
cell(re,'C28','Precio y exposición usan la misma moneda y base de reconocimiento de Economia.');
cell(re,'C29','Vincular componentes a Economia solo una vez. Implantación y expansión pueden requerir otra unidad.');warn(re,'P11:P26');

// Revisión editorial con campos vacíos, sin introducir parámetros empresariales.
for(const s of Object.values(sheets)) {
  s.getUsedRange().format.verticalAlignment='center';
}
wb.recalculate();
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:30},maxChars:3000});
await fs.writeFile(path.join(previews,'revision_formulas.json'),errors.ndjson);
console.log(errors.ndjson);
const ranges={Economia:['C2:N21','C25:N38','C43:I54'],Umbrales:['C2:H29'],Capacidad:['C2:N22','C26:K38'],Caja:['C2:M27'],Existencias:['C2:M22'],Recurrencia:['C2:P22']};
for(const [name,rs] of Object.entries(ranges)) {
  for(let i=0;i<rs.length;i++) {
    const blob=await wb.render({sheetName:name,range:rs[i],scale:1.5,format:'png'});
    await fs.writeFile(path.join(previews,`${name}_${i+1}.png`),new Uint8Array(await blob.arrayBuffer()));
  }
}
const inspect=await wb.inspect({kind:'table',range:'Economia!C10:E15',include:'values,formulas',tableMaxRows:6,tableMaxCols:3,maxChars:3000});
await fs.writeFile(path.join(previews,'revision_vacio.json'),inspect.ndjson);
await fs.writeFile(path.join(previews,'rangos_de_entrada.json'),JSON.stringify(blankInputs,null,2));
const xlsx=await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(path.join(output,'Go2Rev_modelo_economico_v0.1.xlsx'));
try { await fs.rename(path.join(output,'Go2Rev_modelo_economico_v0.1.xlsx.inspect.ndjson'),path.join(previews,'exportacion.inspect.ndjson')); } catch (err) { if(err.code!=='ENOENT') throw err; }
console.log(JSON.stringify({output:'Go2Rev_modelo_economico_v0.1.xlsx',sheets:names.length,review:'Documental; entradas vacías'}));
}
