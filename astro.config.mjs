// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// SITE_URL y BASE_PATH los rellena automáticamente el workflow de GitHub Pages.
// - Repositorio "usuario.github.io" o dominio propio  -> BASE_PATH = "/"
// - Repositorio normal "usuario/maquetas-web"         -> BASE_PATH = "/maquetas-web"
export default defineConfig({
  site: process.env.SITE_URL || 'http://localhost:4321',
  base: process.env.BASE_PATH || '/',
  trailingSlash: 'ignore',
  integrations: [sitemap()],
});
