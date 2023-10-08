# Juego de Meteoritos en Pygame

Este es un juego simple de esquivar meteoritos implementado en Pygame. El jugador controla una nave espacial y debe esquivar los meteoritos mientras dispara para destruirlos. El objetivo es sobrevivir el mayor tiempo posible y ganar puntos destruyendo meteoritos.


![Nuestra Nave Espacial]([https://ejemplo.com/imagen_nave_espacial.png](https://github.com/guilledamian91/meteorite/blob/main/meteorite.jpg))

## Requisitos

- Python 3.x
- Pygame 2.x (Asegúrate de instalarlo antes de ejecutar el juego: `pip install pygame`)
- crear un entorno virtual con pygame antes de ejecutar el juego

## Cómo jugar

- Usa las teclas de flecha izquierda y derecha para mover la nave espacial.
- Presiona la barra espaciadora para disparar láseres y destruir meteoritos.
- El objetivo es evitar que los meteoritos dispaten a la nave espacial.
- Tu puntuación aumenta a medida que destruyes meteoritos.
- La barra de vida en la parte superior muestra la salud actual de la nave espacial.
- El juego termina si la nave espacial se queda sin salud o si se destruyen todos los meteoritos.

## Estructura del código

- El código está dividido en clases para organizar mejor la lógica del juego.
- `Meteor`: Representa los meteoritos que aparecen en pantalla.
- `Player`: Representa la nave espacial controlada por el jugador.
- `Laser`: Representa los láseres disparados por el jugador para destruir meteoritos.
- `MeteorShot`: Representa los disparos de meteoritos que pueden dañar al jugador.
- Hay funciones para la pantalla de inicio (`start_screen()`), pantalla de juego (`victory_screen()`, `game_over_screen()`), y la función principal del juego (`main()`).
- El código utiliza el módulo Pygame para la lógica del juego y la representación visual.

## Personalización

Puedes personalizar el juego modificando los siguientes elementos:

- Las imágenes de los meteoritos, la nave espacial y los láseres. Reemplaza los archivos de imagen en la carpeta `asset` por tus propias imágenes y sonido.
- Ajusta las estadísticas del jugador, como la vida inicial, la velocidad de movimiento y la cantidad de láseres permitidos.
- Modifica la velocidad y el comportamiento de los meteoritos ajustando los valores en la clase `Meteor`.
- Cambia la apariencia de las pantallas de inicio, victoria y derrota modificando las funciones correspondientes.

¡Diviértete personalizando y jugando el juego de meteoritos en Pygame!
