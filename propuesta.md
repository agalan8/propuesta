% E-Shelf
% Alejandro Galán Caballero
% Curso 2024/25

# Descripción general del proyecto

El proyecto consiste en una red social que gira en torno a la fotografía, en esta web los usuarios podrán crear publicaciones en las que publicarán sus mejores fotos, otros usuarios podrán interactuar con estas publicaciones dando me gusta, compartiendo la publicación, comentando... Los usuarios podrán ordenar estas publicaciones en álbumes desde su perfil, además, tendrán una tienda personal donde podrán añadir sus mejores publicaciones para vender. Los usuarios podrán crear comunidades con otros usuarios o unirse a ellas y aportar publicaciones.

## Funcionalidad principal de la aplicación

Red social sobre fotografía.

## Objetivos generales

* Objetivo: "gestionar los usuarios".
* Casos de uso: "registro de cuenta de usuario", "inicio de sesión", "modificar perfil de usuario", "eliminar cuenta de usuario", "mostrar usuarios registrados en la web", "crear usuario", "editar usuario", "eliminar usuario", "ordenar usuarios", "búsqueda en el listado de usuarios", "página de estadísticas de usuario".

* Objetivo: "gestionar las categorías".
* Casos de uso: "crear categoría", "modificar categoría", "eliminar categoría".

* Objetivo: "gestionar las publicaciones e interacciones".
* Casos de uso: "crear publicación", "editar publicación", "eliminar publicación", "mostrar publicaciones de la web", "eliminar publicación (Administrador)", "ordenar publicaciones", "buscar publicaciones en el listado de publicaciones", "dar me gusta a una publicación", "compartir una publicación", "mostrar ubicación de una publicación".

* Objetivo: "gestionar los álbumes y su visualización".
* Casos de uso: "crear álbum", "editar álbum", "eliminar álbum", "añadir publicación a un álbum", "quitar publicaciones de un álbum", "visualizar álbum mediante Flipbook".

* Objetivo: "búsqueda de usuarios, publicaciones y comunidades".
* Casos de uso: "buscar usuarios", "buscar publicaciones", "buscar comunidades".

* Objetivo: "mostrar publicaciones".
* Casos de uso: "página para invitados", "página seguidos".

* Objetivo: "gestionar los amigos y chat".
* Casos de uso: "añadir usuario / ser añadido como amigo", "eliminar amigo", "bloquear usuario", "chat con amigos".

* Objetivo: "gestionar los comentarios".
* Casos de uso: "crear comentario", "editar comentario", "eliminar comentario".

* Objetivo: "gestionar las notificaciones".
* Casos de uso: "centro de notificaciones".

* Objetivo: "gestionar las comunidades".
* Casos de uso: "crear comunidad", "modificar comunidad", "eliminar comunidad", "unirse a una comunidad", "dejar una comunidad", "aportar publicaciones a una comunidad","eliminar publicaciones de una comunidad", "implementar roles de comunidad".

* Objetivo: "gestionar la tienda personal, pagos y carrito".
* Casos de uso: "crear tienda personal", "añadir publicación a tienda personal", "eliminar publicación de tienda personal", "modificar publicación de tienda personal", "implementar plataforma de pago", "añadir publicación al carrito", "eliminar publicación del carrito".

# Elemento de innovación

- Se usará Inertia.js como intermediario para crear una aplicación de una sola página en combinación con React para el desarrollo del frontend.
- Se implementará una librería como Turn.js para crear los Flipbooks.
- Se implementará una librería como Leaflet.js para mostrar en un mapa interactivo la ubicación de las fotos de las publicaciones de los usuarios.
- Se implementará una librería como Stripe para integrar la plataforma de pago en la web.
- Se implementará Laravel Echo + Pusher para integrar el chat con amigos en la web.
- Se implementará una librería como Chart.js para la creación de gráficas para la página de estadísticas de usuario. (Opcional)
