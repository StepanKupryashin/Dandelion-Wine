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
#Настя close 
    image nstl ku happy close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_happy_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_happy_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_ku_happy_close.png"
)

    image nstl ku normal close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_norm_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_norm_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_ku_norm_close.png"
)
    image nstl ku cry close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_pl_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_pl_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_ku_pl_close.png"
)
    image nstl ku sad close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_sad_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_sad_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_ku_sad_close.png"
)
    image nstl ku shy close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_smi_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_smi_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_ku_smi_close.png"
)
    image nstl ku smile close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_smile_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_smile_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_ku_smile_close.png"
)

    image nstl ku shocked close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_ud_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_ud_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_ku_ud_close.png"
)

    image nstl ku angry close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_z_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_ku_z_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_ku_z_close.png"
)

    image nstl pio happy close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_happy_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_happy_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_pio_happy_close.png"
)

    image nstl pio normal close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_norm_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_norm_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_pio_norm_close.png"
)
    image nstl pio cry close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_pl_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_pl_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_pio_pl_close.png"
)

    image nstl pio sad close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_sad_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_sad_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_pio_sad_close.png"
)

    image nstl pio shy close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_smi_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_smi_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_pio_smi_close.png"
)

    image nstl pio smile close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_smile_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_smile_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_pio_smile_close.png"
)

    image nstl pio shocked close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_ud_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_ud_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_pio_ud_close.png"
)

    image nstl pio angry close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_z_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_pio_z_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_pio_z_close.png"
)

    image nstl dress happy close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_happy_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_happy_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_plat_happy_close.png"
)

    image nstl dress normal close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_norm_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_norm_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_plat_norm_close.png"
)

    image nstl dress cry close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_pl_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_pl_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_plat_pl_close.png"
)

    image nstl dress sad close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_sad_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_sad_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_plat_sad_close.png"
)

    image nstl dress shy close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_smi_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_smi_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_plat_smi_close.png"
)

    image nstl dress smile close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_smile_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_smile_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_plat_smile_close.png"
)

    image nstl dress shocked close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_ud_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_ud_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_plat_ud_close.png"
)
    image nstl dress angry close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_z_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_plat_z_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_plat_z_close.png"
)

    image nstl sport happy close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_happy_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_happy_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_sport_happy_close.png"
)

    image nstl sport normal close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_norm_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_norm_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_sport_norm_close.png"
)

    image nstl sport cry close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_pl_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_pl_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_sport_pl_close.png"
)

    image nstl sport sad close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_sad_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_sad_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_sport_sad_close.png"
)

    image nstl sport shy close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_smi_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_smi_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_sport_smi_close.png"
)

    image nstl sport smile close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_smile_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_smile_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_sport_smile_close.png"
)

    image nstl sport shocked close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_ud_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_ud_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_sport_ud_close.png"
)

    image nstl sport angry close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_z_close.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/close/nstl_sport_z_close.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/close/nstl_sport_z_close.png"
)

#Настя far 
    image nstl ku happy far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_happy_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_happy_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_ku_happy_far.png"
)

    image nstl ku normal far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_norm_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_norm_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_ku_norm_far.png"
)
    image nstl ku cry far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_pl_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_pl_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_ku_pl_far.png"
)
    image nstl ku sad far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_sad_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_sad_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_ku_sad_far.png"
)
    image nstl ku shy far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_smi_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_smi_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_ku_smi_far.png"
)
    image nstl ku smile far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_smile_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_smile_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_ku_smile_far.png"
)

    image nstl ku shocked far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_ud_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_ud_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_ku_ud_far.png"
)

    image nstl ku angry far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_z_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_ku_z_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_ku_z_far.png"
)

    image nstl pio happy far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_happy_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_happy_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_pio_happy_far.png"
)

    image nstl pio normal far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_norm_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_norm_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_pio_norm_far.png"
)
    image nstl pio cry far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_pl_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_pl_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_pio_pl_far.png"
)

    image nstl pio sad far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_sad_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_sad_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_pio_sad_far.png"
)

    image nstl pio shy far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_smi_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_smi_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_pio_smi_far.png"
)

    image nstl pio smile far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_smile_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_smile_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_pio_smile_far.png"
)

    image nstl pio shocked far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_ud_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_ud_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_pio_ud_far.png"
)

    image nstl pio angry far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_z_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_pio_z_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_pio_z_far.png"
)

    image nstl dress happy far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_happy_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_happy_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_plat_happy_far.png"
)

    image nstl dress normal far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_norm_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_norm_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_plat_norm_far.png"
)

    image nstl dress cry far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_pl_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_pl_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_plat_pl_far.png"
)

    image nstl dress sad far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_sad_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_sad_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_plat_sad_far.png"
)

    image nstl dress shy far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_smi_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_smi_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_plat_smi_far.png"
)

    image nstl dress smile far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_smile_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_smile_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_plat_smile_far.png"
)

    image nstl dress shocked far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_ud_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_ud_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_plat_ud_far.png"
)
    image nstl dress angry far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_z_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_plat_z_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_plat_z_far.png"
)

    image nstl sport happy far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_happy_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_happy_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_sport_happy_far.png"
)

    image nstl sport normal far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_norm_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_norm_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_sport_norm_far.png"
)

    image nstl sport cry far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_pl_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_pl_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_sport_pl_far.png"
)

    image nstl sport sad far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_sad_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_sad_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_sport_sad_far.png"
)

    image nstl sport shy far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_smi_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_smi_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_sport_smi_far.png"
)

    image nstl sport smile far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_smile_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_smile_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_sport_smile_far.png"
)

    image nstl sport shocked far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_ud_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_ud_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_sport_ud_far.png"
)

    image nstl sport angry far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_z_far.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/far/nstl_sport_z_far.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/far/nstl_sport_z_far.png")

#Настя normal 
    image nstl ku happy normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_happy_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_happy_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_ku_happy_normal.png"
)

    image nstl ku normal normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_norm_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_norm_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_ku_norm_normal.png"
)
    image nstl ku cry normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_pl_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_pl_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_ku_pl_normal.png"
)
    image nstl ku sad normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_sad_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_sad_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_ku_sad_normal.png"
)
    image nstl ku shy normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_smi_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_smi_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_ku_smi_normal.png"
)
    image nstl ku smile normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_smile_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_smile_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_ku_smile_normal.png"
)

    image nstl ku shocked normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_ud_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_ud_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_ku_ud_normal.png"
)

    image nstl ku angry normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_z_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_ku_z_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_ku_z_normal.png"
)

    image nstl pio happy normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_happy_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_happy_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_pio_happy_normal.png"
)

    image nstl pio normal normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_norm_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_norm_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_pio_norm_normal.png"
)
    image nstl pio cry normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_pl_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_pl_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_pio_pl_normal.png"
)

    image nstl pio sad normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_sad_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_sad_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_pio_sad_normal.png"
)

    image nstl pio shy normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_smi_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_smi_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_pio_smi_normal.png"
)

    image nstl pio smile normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_smile_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_smile_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_pio_smile_normal.png"
)

    image nstl pio shocked normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_ud_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_ud_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_pio_ud_normal.png"
)

    image nstl pio angry normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_z_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_pio_z_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_pio_z_normal.png"
)

    image nstl dress happy normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_happy_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_happy_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_plat_happy_normal.png"
)

    image nstl dress normal normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_norm_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_norm_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_plat_norm_normal.png"
)

    image nstl dress cry normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_pl_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_pl_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_plat_pl_normal.png"
)

    image nstl dress sad normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_sad_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_sad_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_plat_sad_normal.png"
)

    image nstl dress shy normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_smi_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_smi_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_plat_smi_normal.png"
)

    image nstl dress smile normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_smile_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_smile_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_plat_smile_normal.png"
)

    image nstl dress shocked normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_ud_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_ud_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_plat_ud_normal.png"
)
    image nstl dress angry normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_z_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_plat_z_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_plat_z_normal.png"
)

    image nstl sport happy normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_happy_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_happy_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_sport_happy_normal.png"
)

    image nstl sport normal normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_norm_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_norm_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_sport_norm_normal.png"
)

    image nstl sport cry normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_pl_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_pl_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_sport_pl_normal.png"
)

    image nstl sport sad normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_sad_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_sad_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_sport_sad_normal.png"
)

    image nstl sport shy normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_smi_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_smi_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_sport_smi_normal.png"
)

    image nstl sport smile normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_smile_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_smile_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_sport_smile_normal.png"
)

    image nstl sport shocked normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_ud_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_ud_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_sport_ud_normal.png"
)

    image nstl sport angry normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_z_normal.png",
                    im.matrix.tint(0.94, 0.82, 1.0)
                    ),
            "persistent.sprite_time=='night'",
                im.MatrixColor(
"mods/MenuTime/sprites/normal/nstl_sport_z_normal.png",
                    im.matrix.tint(0.63, 0.78, 0.82)
                ),
            True,
"mods/MenuTime/sprites/normal/nstl_sport_z_normal.png")





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


