init:
    image nstl pio norm = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_pio_norm.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_pio_norm.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/nstl_pio_norm.png"
)
    image nstl pio z = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_pio_z.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_pio_z.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/nstl_pio_z.png"
)
    image nstl pio smi = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_pio_smi.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_pio_smi.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/nstl_pio_smi.png"
)
    image nstl pio sad = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_pio_sad.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_pio_sad.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/nstl_pio_sad.png"
)
    image nstl pio smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_pio_smile.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_pio_smile.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/nstl_pio_smile.png"
)
    image nstl sport smi = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_sport_smi.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_sport_smi.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/nstl_sport_smi.png"
)
    image nstl pio happy = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_pio_happy.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_pio_happy.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/nstl_pio_happy.png"
)
    image nstl pio normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_pio_norm_norm.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/nstl_pio_norm_norm.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/nstl_pio_norm_norm.png"
)
    image mi sport normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/mi_normal_sport.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/mi_normal_sport.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/mi_normal_sport.png"
)
    image max pi normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/maks_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/maks_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/maks_normal.png"
)
    image max pi serious = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/maks_xz.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/maks_xz.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/maks_xz.png"
)


