import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { Workbook, SpreadsheetFile } from '@oai/artifact-tool';
import { construirModelo } from '../../producto/metodo/oferta_entrega_y_economia/v0.1/modelo/definicion_modelo.mjs';

const here=path.dirname(fileURLToPath(import.meta.url));
await construirModelo({
  Workbook, SpreadsheetFile,
  output:path.resolve(here,'../../producto/metodo/oferta_entrega_y_economia/v0.1/modelo'),
  previews:path.join(here,'salida')
});
