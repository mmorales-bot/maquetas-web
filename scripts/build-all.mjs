// Construye los dos diseños: industrial en la raíz y premium en /premium
import { execSync } from 'node:child_process';
import { rmSync, renameSync } from 'node:fs';

const base = (process.env.BASE_PATH || '/').replace(/\/$/, '');
const run = (cmd, env) => execSync(cmd, { stdio: 'inherit', env: { ...process.env, ...env } });

rmSync('dist', { recursive: true, force: true });
rmSync('dist-premium', { recursive: true, force: true });
run('npx astro build', { THEME: 'industrial', BASE_PATH: base || '/' });
run('npx astro build --outDir dist-premium', { THEME: 'premium', BASE_PATH: `${base}/premium` });
renameSync('dist-premium', 'dist/premium');
console.log('\n✔ Industrial en dist/  ·  Premium en dist/premium/');
