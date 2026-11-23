// ================================================================
//  CONFIGURACIÓN GENERAL DEL SITIO — edita estos datos
// ================================================================
export const SITE = {
  nombre: 'Didactek',
  eslogan: 'Maquetas didácticas de automatización para FP y Universidad',
  descripcion:
    'Catálogo de maquetas y entrenadores didácticos para centros de Formación Profesional y universidades: automatización, electricidad, telecontrol y más.',
  email: 'info@tu-dominio.com',
  telefono: '+34 600 000 000',
  direccion: 'Tu dirección, Ciudad (España)',
  // Formulario de contacto: crea un formulario gratuito en https://formspree.io
  // y pega aquí su URL (p. ej. 'https://formspree.io/f/abcdwxyz').
  // Si lo dejas vacío, el formulario abrirá el programa de correo del visitante.
  formEndpoint: '',
};

// Listas usadas por los filtros del catálogo.
// Deben coincidir con los valores que pongas en cada ficha de maqueta.
export const FAMILIAS = [
  'Electricidad y Electrónica',
  'Instalación y Mantenimiento',
  'Energía y Agua',
  'Informática y Comunicaciones',
  'Fabricación Mecánica',
  'Química',
] as const;

export const NIVELES = ['Grado Medio', 'Grado Superior', 'Universidad'] as const;
