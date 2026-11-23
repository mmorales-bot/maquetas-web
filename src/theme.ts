// Diseño activo. Se elige al construir: THEME=industrial (por defecto) o THEME=premium
export type Theme = 'industrial' | 'premium';
export const THEME: Theme = process.env.THEME === 'premium' ? 'premium' : 'industrial';

// Barra superior para comparar los dos diseños (ponla a false cuando elijas uno)
export const MOSTRAR_SELECTOR_DISENO = true;

// Ruta de cada diseño respecto a la raíz del sitio publicado
export const RUTAS_DISENO: Record<Theme, string> = { industrial: '', premium: 'premium/' };
