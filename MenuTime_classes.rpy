init python:
    from time import strftime
    class Vino_Continue(Action):
        def __call__(self):
            Function(renpy.load(renpy.newest_slot("vino_FilePage_")))
            Function(vino_on_load_callback(renpy.newest_slot("vino_FilePage_")))
        def get_sensitive(self):
            return renpy.newest_slot("vino_FilePage_")


    class ZeroArgs(Exception):
        def __init__(self, data):
            self.data = data

        def __str__(self):
            return repr(self.data) 


    class Vino_ShowMenu(Action,DictEquality):
        def __init__(self,name):
            self.name = name
            self.list = ["vino_preference2","vino_load2","vino_musicroom2","vino_bgmenu2","vino_authors2"]
            if self.name in self.list:
                self.list.remove(self.name)
        def __call__(self):
            for screen in self.list:
                Hide(screen,transition=dissolve)()
            Show(self.name,transition=dissolve)()
        def get_selected(self):
            return renpy.get_screen(self.name)
            
    class Vino_FunctionCallback(Action):
        def __init__(self, function, *arguments):
            self.function = function
            self.arguments = arguments
        def __call__(self):
            return self.function(self.arguments)

    class Vino(object):
        def __init__(self):
            pass

        def change_time(self, target='day'):
            if target == 'day':
                day_time()
                persistent.sprite_time = 'day'
            elif target == 'sunset':
                sunset_time()
                persisstent.sprite_time = 'sunnset'
            elif target == 'night':
                night_time()
                persistent.sprite_time = 'night'

        def set_location(self, location=None, ambience=None, music=None, transition=None, fadein=2, fadeout=2):
            if not location:
                raise ZeroArgs('Введите аргумент location для метода')
            else:
                renpy.scene()
                renpy.show(location)
                if transition:
                    renpy.transition(transition)
            if ambience:
                renpy.music.play(ambience, 'ambience', fadein=fadein, fadeout=fadeout)
            if music:
                    renpy.music.play(music, 'music', fadein=fadein, fadeout=fadeout)


    def vino_nvl_paper(paper='off'):
        """
        paper:str - аключить или выключить режим
        """        
        if paper == 'on':
            renpy.display.screen.screens[("nvl", None)] = renpy.display.screen.screens[("vino_paper_nvl", None)]
            set_mode_nvl()
        elif paper == 'off':
                renpy.display.screen.screens[("nvl", None)] = renpy.display.screen.screens[("vino_nvl", None)]
                set_mode_adv()
    def vino_backdrop(vino_day='День error', vino_bg='mods/MenuTime/gui/backdrop/vino_backdrop_0.jpg', from_vino=True):
        global save_name
        try:
            int(vino_day)
            _window_hide(dissolve)
            renpy.scene()
            if from_vino:
                renpy.show('backdrop_bg', what=Image(vino_bg))
            else:
                renpy.show(vino_bg)
            renpy.pause(2.0, hard=True)
            renpy.show('vino_backdrop_1')
            renpy.transition(dissolve2)
            renpy.pause(3.0, hard=True)
            renpy.show('vino_day_num', what=Text('День ' +str(vino_day), style=style.vino_backdrop_style,xpos=450,ypos=900))
            renpy.transition(dissolve2)
            renpy.pause(5.0, hard=True)
            renpy.scene()
            renpy.show('black')
            renpy.transition(fade2)
            save_name = 'Вино из одуванчиков: День '+str(vino_day)
        except:
            _window_hide(dissolve)
            renpy.scene()
            if from_vino:
                renpy.show('backdrop_bg', what=Image(vino_bg))
            else:
                renpy.show(vino_bg)
            renpy.pause(2.0, hard=True)
            renpy.show('vino_backdrop_1')
            renpy.transition(dissolve2)
            renpy.pause(3.0, hard=True)
            renpy.show('vino_day_num', what=Text(''+str(vino_day), style=style.vino_backdrop_style,xpos=460,ypos=900))
            renpy.transition(dissolve2)
            renpy.pause(5.0, hard=True)
            renpy.scene()
            renpy.show('black')
            renpy.transition(fade2)
            save_name = 'Вино из одуванчиков: '+str(vino_day)

    def vino_main_menu_bg(st,at):
        t = int(strftime('%H')) # Получаем время пользователя.
        if t in range(1,7) or (t in range(20,23)): #Если время пользователя от 1 до 7 или в промежутке от 20 до 23....
            return im.MatrixColor((persistent.vino_bg if persistent.vino_bg != None else 'mods/MenuTime/gui/menu/vino_bg.jpg'), im.matrix.tint(0.15, 0.18, 0.19)*im.matrix.brightness(-0.015)), 0.1 #Возращаем изображение бг меню, с эффектом затемнения.
        else:
            return Image((persistent.vino_bg if persistent.vino_bg != None else 'mods/MenuTime/gui/menu/vino_bg.jpg')), 0.1 #Иначе возвращается обычное изображение

    renpy.image('vino_menu_bg', DynamicDisplayable(vino_main_menu_bg))

    def vino_time(st, at):
        t = strftime('%H:%M')
        h = int(strftime('%H'))
        if h in range(0,7) or (h in range(20, 24)):
            return Text(str(t), style=style.vino_text_night), 0.1
        else:
            return Text(str(t), style=style.vino_text_day), 0.1

    renpy.image('vino_time', DynamicDisplayable(vino_time))

    def vino_get_time(full=False):
        t = int(strftime('%H'))
        if t in range(0,7) or (t in range(20,24)): #Если время пользователя от 1 до 7 или в промежутке от 20 до 23....
            return 'night'
        else:
            return "day"
    vino = Vino()


