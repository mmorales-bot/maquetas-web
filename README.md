# Web de maquetas didácticas

Catálogo web de maquetas y entrenadores didácticos para centros de Formación Profesional y universidades.
Hecho con [Astro](https://astro.build) (web estática) y publicado gratis en GitHub Pages.

## Editar los datos generales

Abre `src/site.config.ts` y cambia nombre, eslogan, email, teléfono, dirección y el endpoint del formulario.

### Formulario de contacto
1. Crea una cuenta gratuita en <https://formspree.io> y un formulario nuevo.
2. Copia su URL (p. ej. `https://formspree.io/f/abcdwxyz`) en `formEndpoint`.
3. Si lo dejas vacío, el botón "Enviar" abre el programa de correo del visitante.

## Añadir una maqueta nueva

1. Copia un archivo de `src/content/maquetas/` (p. ej. `entrenador-plc.md`) y renómbralo.
   El nombre del archivo será la dirección de la ficha: `mi-maqueta.md` → `/maquetas/mi-maqueta`.
2. Edita la cabecera (entre `---`):
   - `titulo`, `referencia`, `resumen`, `tematica`
   - `imagen`: ruta a una foto dentro de `public/` (p. ej. `img/mi-maqueta.jpg`)
   - `familias` y `niveles`: deben ser valores de las listas de `src/site.config.ts`
   - `destacada: true` para que salga en la portada; `orden` para ordenarla
   - `especificaciones`, `ciclos` y `documentos` (PDFs dentro de `public/docs/`)
3. Debajo de la cabecera escribe la descripción en Markdown.
4. Guarda y sube los cambios a GitHub: la web se republica sola en 1-2 minutos.

Todo se puede hacer desde la propia web de GitHub (botón "Add file" / icono de lápiz), sin instalar nada.

## Trabajar en local (opcional)

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # genera la web en dist/
```

## Publicación

Cada `push` a la rama `main` ejecuta `.github/workflows/deploy.yml` y publica la web.
Primera vez: en el repositorio de GitHub ve a **Settings → Pages → Source: GitHub Actions**.

### Dominio propio
En **Settings → Pages → Custom domain** escribe tu dominio y crea en tu proveedor DNS
un registro `CNAME` apuntando a `TU-USUARIO.github.io`.
