init python:


    ####################
    style.vino_button_none = Style(style.button)
    style.vino_button_none.background = None
    style.vino_button_none.hover_background = None
    style.vino_button_none.selected_background = None
    style.vino_button_none.selected_hover_background = None
    style.vino_button_none.selected_idle_background = None

    style.vino_text = Style(style.default)
    style.vino_text.font = "mods/MenuTime/vino_font.ttf"
    style.vino_text.size = 60
    style.vino_text.color = "#FFFFFF"
    style.vino_text.hover_color = "#EB0707"
    style.vino_text.selected_color = "#EB0707"



    style.vino_text_set_bg = Style(style.default)
    style.vino_text_set_bg.font = "mods/MenuTime/vino_font.ttf"
    style.vino_text_set_bg.size = 40
    style.vino_text_set_bg.color = "#FFFFFF"
    style.vino_text_set_bg.hover_color = "#EB0707"
    style.vino_text_set_bg.selected_color = "#EB0707"

    style.vino_text_big_save_load                          = Style(style.default)
    style.vino_text_big_save_load.font                     = 'mods/MenuTime/vino_font.ttf'
    style.vino_text_big_save_load.size                     = 80
    style.vino_text_big_save_load.color                    = "#ffffff"
    style.vino_text_big_save_load.hover_color              = "#EB0707"
    style.vino_text_big_save_load.selected_color           = "#ffffff"
    style.vino_text_big_save_load.selected_idle_color      = "#ffffff"
    style.vino_text_big_save_load.selected_hover_color     = "#EB0707"
    style.vino_text_big_save_load.insensitive_color        = "#ffffff"

    style.vino_save_load_button                            = Style(style.button)
    style.vino_save_load_button.background                 = 'mods/MenuTime/gui/save_load/Save_Load_Button_idle.png'
    style.vino_save_load_button.hover_background           = 'mods/MenuTime/gui/save_load/Save_Load_Button_hover.png'
    style.vino_save_load_button.selected_background        = 'mods/MenuTime/gui/save_load/Save_Load_Button_selected.png'
    style.vino_save_load_button.selected_hover_background  = 'mods/MenuTime/gui/save_load/Save_Load_Button_selected.png'
    style.vino_save_load_button.selected_idle_background   = 'mods/MenuTime/gui/save_load/Save_Load_Button_selected.png'

    style.vino_backdrop_style = Style(style.default)
    style.vino_backdrop_style.font = 'mods/MenuTime/vino_backdrop_font.ttf'
    style.vino_backdrop_style.color = '#FFFF'
    style.vino_backdrop_style.size = 80
    style.vino_backdrop_style.bold = True
    style.vino_backdrop_style.outlines = [ (absolute(2), '#282828', absolute(1), absolute(1))]

    style.vino_game_menu_selector_day = Style(style.default)
    style.vino_game_menu_selector_day.font = "mods/MenuTime/vino_font.ttf"
    style.vino_game_menu_selector_day.size = 35
    style.vino_game_menu_selector_day.color = '#73c1e3'
    style.vino_game_menu_selector_day.hover_color = '#355572'
    ########################################
    style.vino_game_menu_selector_night = Style(style.default)
    style.vino_game_menu_selector_night.font = "mods/MenuTime/vino_font.ttf"
    style.vino_game_menu_selector_night.size = 35
    style.vino_game_menu_selector_night.color = '#2226af'
    style.vino_game_menu_selector_night.hover_color = '#1c1e4e'
    #######################################
    style.vino_game_menu_selector_prologue = Style(style.default)
    style.vino_game_menu_selector_prologue.font = "mods/MenuTime/vino_font.ttf"
    style.vino_game_menu_selector_prologue.size = 35
    style.vino_game_menu_selector_prologue.color = '#2226af'
    style.vino_game_menu_selector_prologue.hover_color = '#1c1e4e'
    #########################################################
    style.vino_game_menu_selector_sunset = Style(style.default)
    style.vino_game_menu_selector_sunset.font = "mods/MenuTime/vino_font.ttf"
    style.vino_game_menu_selector_sunset.size = 35
    style.vino_game_menu_selector_sunset.color = '#fcbab1'
    style.vino_game_menu_selector_sunset.hover_color = '#ab5450'
    ##########################################
    style.vino_play_music_text = Style(style.default)
    style.vino_play_music_text.font = "mods/MenuTime/vino_font.ttf"
    style.vino_play_music_text.size = 60
    style.vino_play_music_text.color = "#FFFFFF"
    style.vino_play_music_text.hover_color = "#EB0707"
    style.vino_play_music_text.selected_color = "#EB0707"
    style.vino_play_music_text.outlines = [ (absolute(2), '#696969', absolute(1), absolute(1))] 
    #########################################

    
transform vino_button_anim:
    on idle:
        ease 0.5 zoom 1.00
    on hover:
        ease 0.5 zoom 1.05
transform vino_menu_anim:
    zoom 1.2 align(0.5,0.5)
    block:
        ease 3.0 align(0.5,0.3)
        ease 3.0 align(0.8,0.6)
        ease 3.0 align(0.4,0.2)
        repeat
transform vino_on_show_authors_menu:
    on hide:
        xalign 0.5 
        yalign 0.5
        linear 2.5 xoffset 2000
transform vino_on_show_main_menu:
    on hide:
        xalign 0.5 
        yalign 0.5
        linear 2.5 yoffset 2000
transform vino_plate_anim:
    subpixel True
    zoom 0.7
    anchor(0.5,0.5)
    on idle:
        ease 0.3 zoom 0.7
        block:
            linear 8.0 rotate 360.0
            rotate 0.0
            repeat
    on hover:
        ease 0.3 zoom 0.8 rotate 0.0

init:

    $ config.developer = True

    $ dnll = Character (u'Даниил', color = "00FF7F", what_color="f2f2f2")
    $ momsd= Character (u'Мама', color = "00BFFF", what_color="f2f2f2")
    $ loxqt= Character (u'Миша', color = "DB7093", what_color="f2f2f2")
    $ nstl = Character(u'Настя', color = "00FFFF", what_color="f2f2f2")
    $ neznakqqwy = Character (u'...', color = "DB7093", what_color="f2f2f2")
    define mimikumi = Character('Я', kind=nvl, color="#c8c8ff")
    $ xzktoqtwqwe = Character (u'Отголоски', color = "191970", what_color="f2f2f2")
    $ silxvahfy = Character (u'Силуэт', color = "FF1493", what_color="f2f2f2")
    $ mirasll = Character (u'...', color = "00deff")
    $ mamecki = Character (u'Мама', color = "4682B4")
    $ otecki = Character (u'Папа', color = "4169E1")
    $ evgnll = Character (u'Евгений', color = "9400D3")
    $ elmisl = Character (u'...', color = "ffff00")
    $ macksya = Character (u'Макс', color = "d41114")
    define nei = Character('...', kind=nvl, color="#00deff")
    define danilg = Character('Даниил', kind=nvl, color="#00FF7F")
    define misskaty = Character('Катя', kind=nvl, color="#556B2F")
    define loxqr = Character('Миша', kind=nvl, color="#DB7093")
    $ povr = Character(u'Повар', color="ffff00")
    
    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # центральная позиция
                self.dist = dist    # максимальное расстояние, в пикселях, от начальной точки
                self.child = child
                
            def __call__(self, t, sizes):
                # Число с плавающей точкой в целое число... превращает числа с плавающей точкой
                # в целые.      
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)

    $ mods["vino1"]=u"{b}Вино из одуванчиков.{/b}"
    
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    
    transform vio_runn():
        anchor (0.0, 0.0) pos (0.0, 0.0)
        linear 0.1 pos (-6, -5)
        linear 0.1 pos (0, 0)
        linear 0.1 pos (-6, -5)
        linear 0.1 pos (0, 0)
        repeat
    
    transform vio_sit_center:
        xalign 0.5
        yanchor 0.0
        ypos 0.22
    
    transform vio_get_up_fast:
        subpixel True
        parallel:
            ease 0.3 ypos 0.0
        parallel:
            ease 0.2 zoom 1.05
            ease 0.07 zoom 1.0
    