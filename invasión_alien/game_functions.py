#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from time import sleep
import pygame
from bala import Bala
from alien import Alien


def check_keydown_events(event, ai_ajustes, pantalla, nave, balas):
    """Respuesta a cuando se oprime algun boton."""

    if event.key == pygame.K_ESCAPE:
        pause()
    elif event.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_ajustes, pantalla, nave, balas)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.type == pygame.QUIT:
        sys.exit()


def pause():
    """Función de pausar el juego."""
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False


def check_keyup_events(event, nave):
    """Respuesta a cuando se deja de oprimir una tecla"""
    if event.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False


def check_events(ai_ajustes, pantalla, estadisticas, sb, play_button, nave, aliens,
                 balas):
    """Responder a eventos del teclado y mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_ajustes, pantalla, nave, balas)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, nave)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_ajustes, pantalla, estadisticas, sb, play_button,
                              nave, aliens, balas, mouse_x, mouse_y)


def check_play_button(ai_ajustes, pantalla, estadisticas, sb, play_button,
                      nave, aliens, balas, mouse_x, mouse_y):
    """Iniciar cuando se oprime el boton de play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not estadisticas.game_active:
        # Restablecer los ajustes.
        ai_ajustes.initialize_dynamic_settings()

        # Ocultar mouse.
        pygame.mouse.set_visible(False)

        # Restablecer estadisticas del juego.
        estadisticas.reset_stats()
        estadisticas.game_active = True

        # Restablecer imagenes del marcador.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Vaciar la lista de alienígenas y balas.
        aliens.empty()
        balas.empty()

        # Crear nuevo grupo de aliens y centrar la nave.
        create_fleet(ai_ajustes, pantalla, nave, aliens)
        nave.center_ship()


def fire_bullet(ai_ajustes, pantalla, nave, balas):
    """Disparar bala si no se ha llegado al limite."""
    # Crear nueva bala, agregar grupo de balas..
    if len(balas) < ai_ajustes.bullets_allowed:
        bala_nueva = Bala(ai_ajustes, pantalla, nave)
        balas.add(bala_nueva)


def update_screen(ai_ajustes, pantalla, estadisticas, sb, nave, aliens,
                  balas, play_button, mensaje_go):
    """Actualizar imagenes en la pantalla."""
    # redibujar la pantalla con cada bucle.
    fondo = pygame.image.load("images/fondo.png").convert()
    pantalla.blit(fondo, [0, 0])
    sonido_go = pygame.mixer.Sound("382310__myfox14__game-over-arcade.wav")

    # Redibujar todas las balas.
    for bala in balas.sprites():
        bala.dibujo_bala()
    nave.blitme()
    aliens.draw(pantalla)

    # Dibujar puntuacion.
    sb.show_score()

    # Dibujar boton de star cuando el juego no esta corriendo.
    if not estadisticas.game_active:
        play_button.draw_button()
        if estadisticas.ships_left == 0:
            sonido_go.play(loops=0)
            mensaje_go.draw_msg()

    # Mostrar la pantalla actualizada.
    pygame.display.flip()


def update_bullets(ai_ajustes, pantalla, estadisticas, sb, nave, aliens,
                   balas):
    """Actualizar la posicion de las balas, eliminar balas viejas."""
    # Mantener actualizada la posicion de las balas.
    balas.update()

    # Borrar las balas que ya no se ven.
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)

    check_bullet_alien_collisions(ai_ajustes, pantalla, estadisticas, sb, nave,
                                  aliens, balas)


def check_high_score(estadisticas, sb):
    """Cambiar la mejor puntuacion."""
    if estadisticas.score > estadisticas.high_score:
        estadisticas.high_score = estadisticas.score
        sb.prep_high_score()


def check_bullet_alien_collisions(ai_ajustes, pantalla, estadisticas, sb, nave,
                                  aliens, balas):
    """Respuesta a la colisión bala-alien."""
    # Quitar al alien y a la bala una vez que se de la colisión.
    collisions = pygame.sprite.groupcollide(balas, aliens, True, True)
    sonido_colisión = pygame.mixer.Sound("collision.wav")
    if collisions:
        sonido_colisión.play()
        for aliens in collisions.values():
            estadisticas.score += ai_ajustes.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(estadisticas, sb)

    if len(aliens) == 0:
        # El nivel debe cambiar cuando se eliminan todos los aliens.
        balas.empty()
        ai_ajustes.increase_speed()

        # Incrementar el nivel.
        estadisticas.level += 1
        sb.prep_level()

        create_fleet(ai_ajustes, pantalla, nave, aliens)


def check_fleet_edges(ai_ajustes, aliens):
    """Respuesta al hecho de que un alien llegué al borde."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_ajustes, aliens)
            break


def change_fleet_direction(ai_ajustes, aliens):
    """Cambiar la dirección de toda la flota de aliens."""
    for alien in aliens.sprites():
        alien.rect.y += ai_ajustes.fleet_drop_speed
    ai_ajustes.fleet_direction *= -1


def ship_hit(ai_ajustes, pantalla, estadisticas, sb, nave, aliens, balas,
             mensaje_go):
    """Respuesta si la nave es golpeada por un alien."""
    if estadisticas.ships_left > 0:
        # Quitar una vida.
        estadisticas.ships_left -= 1

        # Actualizar la pizarra de puntaje.
        sb.prep_ships()

    if estadisticas.ships_left == 0:
        estadisticas.game_active = False
        mensaje_go.draw_msg()
        pygame.mouse.set_visible(True)

    # Vaciar la lista de aliens y balas.
    aliens.empty()
    balas.empty()

    # Crear otra flota y volver a centrar la nave.
    create_fleet(ai_ajustes, pantalla, nave, aliens)
    nave.center_ship()

    # Pausa antes de empezar de nuevo.
    sleep(0.5)


def check_aliens_bottom(ai_ajustes, pantalla, estadisticas, sb, nave, aliens,
                        balas, mensaje_go):
    """Comprobar si algún alien llegó al  borde inferior de la pantalla"""
    screen_rect = pantalla.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Debe ser igual al evento de la nave golpeada por un alien.
            ship_hit(ai_ajustes, pantalla, estadisticas, sb, nave, aliens,
                     balas, mensaje_go)
            break


def update_aliens(ai_ajustes, pantalla, estadisticas, sb, nave, aliens, balas,
                  mensaje_go):
    """Efectuar las funciones necesarias, una vez que se ha perdido."""

    check_fleet_edges(ai_ajustes, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(nave, aliens):
        ship_hit(ai_ajustes, pantalla, estadisticas, sb, nave, aliens, balas,
                 mensaje_go)

    check_aliens_bottom(ai_ajustes, pantalla, estadisticas, sb, nave, aliens,
                        balas, mensaje_go)


def get_number_aliens_x(ai_ajustes, alien_ancho):
    """Determinar la cantidad de aliens que caben en una fila."""
    espacio_disponible = ai_ajustes.screen_width - 2 * alien_ancho
    cantidad_aliens = int(espacio_disponible / (2 * alien_ancho))
    return cantidad_aliens


def get_number_rows(ai_ajustes, nave_altura, alien_altura):
    """Determinar la cantidad de filas de aliens que caben en la pantalla."""
    espacio_disponible_y = (ai_ajustes.screen_height -
                            (3 * alien_altura) - nave_altura)
    cantidad_filas = int(espacio_disponible_y / (2 * alien_altura))
    return cantidad_filas


def create_alien(ai_ajustes, pantalla, aliens, numero_de_alien,
                 cantidad_filas):
    """Crear al alien y ubicarlo en la fila."""
    alien = Alien(ai_ajustes, pantalla)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * numero_de_alien
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * cantidad_filas
    aliens.add(alien)


def create_fleet(ai_ajustes, pantalla, nave, aliens):
    """Crear la flota de aliens."""

    alien = Alien(ai_ajustes, pantalla)
    cantidad_aliens = get_number_aliens_x(ai_ajustes, alien.rect.width)
    cantidad_filas = get_number_rows(ai_ajustes, nave.rect.height,
                                     alien.rect.height)

    for numero_de_fila in range(cantidad_filas):
        for numero_de_alien in range(cantidad_aliens):
            create_alien(ai_ajustes, pantalla, aliens, numero_de_alien,
                         numero_de_fila)
