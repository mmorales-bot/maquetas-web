import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { FAMILIAS, NIVELES } from './site.config';

const maquetas = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/maquetas' }),
  schema: z.object({
    titulo: z.string(),
    referencia: z.string(),
    resumen: z.string(),
    imagen: z.string(),
    familias: z.array(z.enum(FAMILIAS)).min(1),
    niveles: z.array(z.enum(NIVELES)).min(1),
    tematica: z.string(),
    destacada: z.boolean().default(false),
    especificaciones: z.array(z.object({ nombre: z.string(), valor: z.string() })).default([]),
    ciclos: z.array(z.string()).default([]),
    documentos: z.array(z.object({ titulo: z.string(), archivo: z.string() })).default([]),
    orden: z.number().default(100),
  }),
});

export const collections = { maquetas };
