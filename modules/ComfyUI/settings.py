# env start_tool.py/py
# -*- coding: UTF-8 -*-
'''
@Project ：start_tool.py 
@File    ：settings.py
@IDE     ：PyCharm 
@Author  ：Mr数据杨
@Date    ：2024-11-07 8:03 
'''

import random


# 外观描述
class AppearanceDescription:
    @staticmethod
    def BasePrompt(gender, body_type, skin_tone, regional, hair_style, hair_color):
        prompt = f"""
        You are an AI drawing assistant with rich imagination, good at describing various pictures, and accustomed to providing stable diffusion as prompts. I give you a text description of clothes. 
        You need to add this pile of clothes to a {gender} model with a {body_type} body, {skin_tone} skin tone, {regional}, and {hair_style} hair styled in a {hair_color} shade. 
        The scene should vividly capture the essence of this model in the described outfit, ensuring the outfit’s details are unchanged.
        
        Based on the previous description, please write a detailed description of the three views of the model in the following format:
        
        Left picture (Show the model from the left side, not the front of the face): a side profile photo of a {body_type} {regional} {gender} with {skin_tone} skin tone, styled with {hair_style} hair in a {hair_color} shade. The clothing should be fully described without any missing items, ensuring the details are accurate from this angle;
        
        Image on the middle side (front view): A full-body photo of a {body_type} {regional} {gender} from the front, with {skin_tone} skin tone, and {hair_style} hair styled in a {hair_color} shade. The clothing must be fully described without any missing items, capturing all front-facing details of the outfit;
        
        Right image (back of the person, no need to describe facial expression): A full-body photo of a {body_type} {regional} {gender} from the back, with {skin_tone} skin tone, and {hair_style} hair styled in a {hair_color} shade. The clothing must be fully described without any missing items, capturing all details from the back view.
        """

        return prompt

    @staticmethod  # 性别
    def Gender():
        data = [
            {"key":"男性", "value":"male", "description":"男性角色"},
            {"key":"女性", "value":"female", "description":"女性角色"},
            {"key":"中性", "value":"androgynous", "description":"中性的性别特征"},
        ]
        return data

    @staticmethod  # 身材
    def BodyType():
        data = [
            {"key":"瘦削", "value":"slender", "description":"整体较为瘦长，骨架轻，肌肉线条不明显，身形修长而纤细，显得轻盈优雅，适合打造精致、细致的角色形象"},
            {"key":"健美", "value":"muscular", "description":"身形肌肉发达，具备清晰的肌肉线条，体现出力量和健康的美感，适合表现力量型角色或运动员等形象"},
            {"key":"丰满", "value":"curvy", "description":"身材曲线明显，身体线条柔和且饱满，拥有较宽的胸部和臀部，适合表现温柔、成熟或性感的角色特质"},
            {"key":"苗条", "value":"slim", "description":"身形轻盈但带有适当的曲线，身材匀称，没有明显的肌肉或脂肪，呈现出优雅自然的美感，适合温柔、朴素的角色"},
            {"key":"粗壮", "value":"stocky", "description":"身形矮壮，骨架较宽，通常带有较厚的肌肉或脂肪层，给人一种厚实、坚韧的感觉，适合具有力量感的角色"},
            {"key":"娇小", "value":"petite", "description":"身材小巧玲珑，整体比例较短小，身形纤细，给人一种可爱、灵活的感觉，适合可爱或年轻的角色"},
            {"key":"高大", "value":"tall", "description":"身形高挑，比一般身材更为修长，适合高大、英俊或威严的角色"},
            {"key":"肥胖", "value":"obese", "description":"身材肥胖，脂肪堆积明显，整体轮廓圆润，适合刻画慵懒或富态的角色"},
            {"key":"肌肉型", "value":"athletic", "description":"身材匀称而结实，肌肉发达但不过于夸张，体现健康和活力，适合运动型角色"},
            {"key":"中等身材", "value":"average", "description":"普通身材，没有过多的肌肉或脂肪，比例匀称，适合一般角色形象"},
            {"key":"骨感", "value":"skinny", "description":"体型极瘦，骨架明显，缺乏肌肉，整体看起来清瘦，适合展现瘦弱或纤细的角色"},
            {"key":"壮硕", "value":"broad", "description":"肩膀宽厚，体格壮实，常用于表现力量型或保护者形象的角色"},
            {"key":"矮小", "value":"short", "description":"身高较低，适合表现年轻、灵活或轻盈的角色，具有俏皮或年轻感"},
            {"key":"结实", "value":"firm", "description":"整体肌肉紧实，略微显得强壮，适合表现健美但不过分强壮的形象"},
            {"key":"苗条健美", "value":"lean", "description":"身形修长且肌肉匀称，适合运动员或具有精瘦特质的角色"},
            {"key":"圆润", "value":"plump", "description":"身体稍显圆润，但不是过度肥胖，适合表现柔和或平易近人的角色"},
            {"key":"纤弱", "value":"delicate", "description":"身体娇弱，看起来纤细脆弱，适合温柔或需要保护的角色"},
            {"key":"优雅", "value":"graceful", "description":"身材修长优雅，举止端庄得体，适合表现高贵或优雅的角色"},
            {"key":"结实厚重", "value":"heavyset", "description":"体型厚重，通常伴有一些脂肪，适合表现厚实、沉稳的形象"},
            {"key":"肌肉紧致", "value":"toned", "description":"肌肉紧致但不过分隆起，展示健康活力的体型，适合普通运动爱好者形象"},
        ]
        return data

    @staticmethod  # 肤色
    def SkinTone():
        data = [
            {"key":"白皙", "value":"fair", "description":"非常白皙、透明的肤色，带有轻微的粉色调，适合表现高贵、纯洁或精致的角色形象"},
            {"key":"象牙白", "value":"ivory", "description":"带有温暖调的白色肤色，比白皙肤色稍深，但依然显得清透，适合表现自然且柔和的形象"},
            {"key":"健康小麦色", "value":"tan", "description":"带有自然的日晒色，呈现出健康的小麦色调，适合运动、户外活动多的角色"},
            {"key":"淡褐色", "value":"light brown", "description":"淡淡的棕色肤色，比小麦色稍深，适合展现温暖和友善的形象"},
            {"key":"棕色", "value":"brown", "description":"较深的棕色皮肤，带有浓厚的暖色调，适合表现成熟、稳重的角色"},
            {"key":"深褐色", "value":"dark brown", "description":"深色的褐色皮肤，色调浓郁而富有质感，适合表现力量感或神秘感的角色"},
            {"key":"黑色", "value":"dark", "description":"深黑色的皮肤，非常浓郁，适合表现厚重、庄严的角色气质"},
            {"key":"蜜色", "value":"honey", "description":"温暖的蜜色皮肤，带有淡金色光泽，适合表现阳光温柔的角色形象"},
            {"key":"橄榄色", "value":"olive", "description":"带有淡绿色调的中性色肤色，常见于地中海地区，适合表现异域风情的角色"},
            {"key":"古铜色", "value":"bronze", "description":"带有金属光泽的古铜色皮肤，呈现出强烈的健康活力感，适合塑造强壮、自信的角色"},
            {"key":"粉色调", "value":"rosy", "description":"白皙皮肤中带有粉色调，显得皮肤细腻娇嫩，适合表现年轻、柔美的角色"},
            {"key":"奶油色", "value":"cream", "description":"奶油般柔和的浅肤色，适合温柔、可爱型的角色，给人一种温暖舒适的感觉"},
            {"key":"亚麻色", "value":"linen", "description":"极为浅淡、略带黄色调的白色，适合表现中立、温和的形象"},
            {"key":"古老棕褐色", "value":"dusky", "description":"略带冷色调的棕褐色，常用于表现带有神秘感或沧桑感的角色"},
            {"key":"冷调白皙", "value":"pale", "description":"比白皙更苍白的肤色，通常带有些许冷色调，适合表现虚弱、神秘或高贵的角色"},
            {"key":"灰褐色", "value":"ashen", "description":"灰色调的褐色，适合表现略带病态或忧郁气质的角色"},
            {"key":"浅琥珀色", "value":"amber", "description":"带有琥珀色光泽的皮肤，介于棕色和橙色之间，适合塑造温暖、友善的角色"},
            {"key":"黄皮", "value":"yellow", "description":"带有黄色调的皮肤，通常用来表现亚洲地区特征，适合自然、亲和力强的角色"},
            {"key":"金褐色", "value":"golden brown", "description":"带有金黄色泽的深褐色，适合表现奢华、迷人或阳光型的角色"},
        ]
        return data

    @staticmethod  # 地区
    def Regional():
        data = [
            {"key":"东亚", "value":"East Asian", "description":"具有东亚地区特征，如中国、日本、韩国，皮肤通常偏白或略带黄色调，面部特征柔和，适合表现传统或现代亚洲形象"},
            {"key":"东南亚", "value":"Southeast Asian", "description":"来自东南亚的特征，如泰国、越南、菲律宾等，肤色通常为小麦色或淡褐色，面部五官略带异域感"},
            {"key":"南亚", "value":"South Asian", "description":"南亚特征，如印度、巴基斯坦等地区，肤色偏深至褐色，五官立体，适合塑造充满异域风情的角色"},
            {"key":"中东", "value":"Middle Eastern", "description":"中东地区特征，如阿拉伯、伊朗等，皮肤通常是橄榄色或深褐色，五官深邃，带有浓厚的文化和宗教氛围"},
            {"key":"北非", "value":"North African", "description":"具有北非特征，如埃及、摩洛哥，肤色多为浅棕色或深褐色，五官深邃，适合表现历史和文化气息浓厚的角色"},
            {"key":"撒哈拉以南非洲", "value":"Sub-Saharan African", "description":"撒哈拉以南非洲地区特征，皮肤通常较深，带有黑色或深褐色的浓厚肤色，适合塑造具有活力、力量感的角色"},
            {"key":"西欧", "value":"Western European", "description":"西欧特征，如英国、法国、德国，皮肤多为白皙或浅色，五官立体，适合表现现代、经典或贵族气质的角色"},
            {"key":"东欧", "value":"Eastern European", "description":"东欧地区特征，如俄罗斯、波兰、乌克兰，肤色多为白皙或略带红润，五官立体分明，适合表现冷峻或严谨的角色"},
            {"key":"北欧", "value":"Nordic", "description":"北欧地区特征，如挪威、瑞典、芬兰，皮肤通常白皙，头发多为浅色，适合塑造高大、冷艳或优雅的角色"},
            {"key":"南欧", "value":"Southern European", "description":"南欧特征，如意大利、西班牙、希腊，肤色偏浅棕或小麦色，适合表现热情、阳光或浪漫的形象"},
            {"key":"拉丁美洲", "value":"Latin American", "description":"拉丁美洲特征，如墨西哥、巴西、阿根廷，肤色多为小麦色至深褐色，五官富有热情，适合表现活力、热情的角色"},
            {"key":"加勒比地区", "value":"Caribbean", "description":"加勒比地区特征，肤色偏深或中等褐色，适合展现热情洋溢、自由奔放的形象"},
            {"key":"北美", "value":"North American", "description":"北美特征，如美国和加拿大，肤色多样，从白皙到深色，适合现代、个性化的角色"},
            {"key":"大洋洲", "value":"Oceanian", "description":"大洋洲特征，如澳大利亚、新西兰及太平洋岛国，肤色多为浅棕或中等褐色，适合展现自由、自然的角色形象"},
            {"key":"中亚", "value":"Central Asian", "description":"中亚地区特征，如哈萨克斯坦、乌兹别克斯坦，肤色中等褐色，带有高颧骨等特色，适合表现神秘、悠远的角色"},
            {"key":"美洲土著", "value":"Indigenous American", "description":"美洲土著特征，肤色多为深褐色至中等褐色，面部特征具有民族特性，适合表现自然、朴实的形象"},
            {"key":"非洲裔", "value":"African descent", "description":"非洲裔特征，通常为深色皮肤，面部轮廓明显，适合表现坚韧、自信的形象"},
            {"key":"阿拉伯裔", "value":"Arab", "description":"阿拉伯裔特征，肤色从浅褐色到深褐色，适合表现中东和北非的文化特色和深邃的面部表情"},
            {"key":"南非裔", "value":"Southern African", "description":"南非裔特征，肤色深至黑色，面部轮廓明显，适合表现坚韧、乐观的形象"},
        ]
        return data

    @staticmethod  # 发色
    def HairColor():
        data = [
            {"key":"黑色", "value":"black", "description":"深邃的黑色头发，光泽感强，适合展现神秘、优雅或稳重的角色"},
            {"key":"深棕色", "value":"dark brown", "description":"接近黑色的深棕色，温暖而柔和，适合自然且成熟的角色"},
            {"key":"浅棕色", "value":"light brown", "description":"较浅的棕色，温暖且亲和，适合表现自然、随和的角色形象"},
            {"key":"栗色", "value":"chestnut", "description":"带有红色调的棕色，温暖而有活力，适合热情、温柔的角色"},
            {"key":"金色", "value":"blonde", "description":"明亮的金色头发，带有阳光般的光泽，适合塑造活泼、热情或高贵的角色"},
            {"key":"灰白色", "value":"gray", "description":"略带银色的灰白色，适合塑造成熟、智慧或沧桑感的角色"},
            {"key":"银色", "value":"silver", "description":"纯银色的头发，具有高贵、神秘的气质，适合幻想或古老的角色形象"},
            {"key":"红色", "value":"red", "description":"浓烈的红色头发，充满激情和活力，适合塑造个性鲜明的角色"},
            {"key":"深红色", "value":"auburn", "description":"带有棕色调的深红色，温暖而迷人，适合表现成熟且稳重的角色"},
            {"key":"橙色", "value":"orange", "description":"明亮的橙色头发，活泼而醒目，适合表现独特、个性化的角色"},
            {"key":"玫瑰金", "value":"rose gold", "description":"带有粉色调的金色，温柔而独特，适合塑造浪漫、梦幻的形象"},
            {"key":"粉色", "value":"pink", "description":"活泼的粉色头发，充满幻想，适合表现可爱、甜美或前卫的角色"},
            {"key":"蓝色", "value":"blue", "description":"鲜明的蓝色头发，具有冷酷的美感，适合塑造神秘或异世界的角色"},
            {"key":"深蓝色", "value":"dark blue", "description":"深邃的蓝色头发，带有冷峻的气质，适合表现冷酷或沉稳的角色"},
            {"key":"紫色", "value":"purple", "description":"神秘的紫色头发，带有幻想色彩，适合塑造具有魔幻气质的角色"},
            {"key":"浅紫色", "value":"lavender", "description":"淡紫色的头发，温柔且优雅，适合浪漫、柔和的角色形象"},
            {"key":"绿色", "value":"green", "description":"生动的绿色头发，充满自然气息，适合表现与自然融为一体的角色"},
            {"key":"浅绿色", "value":"mint green", "description":"带有薄荷色调的绿色，清新自然，适合活泼或清新型角色"},
            {"key":"黄褐色", "value":"dirty blonde", "description":"介于棕色和金色之间的混合色，适合塑造亲和、自然的角色"},
            {"key":"白色", "value":"white", "description":"纯白色的头发，给人高洁或神秘的感觉，适合塑造幻想或异世风格的角色"},
            {"key":"银蓝色", "value":"silver blue", "description":"带有蓝色光泽的银色头发，冷艳而神秘，适合塑造梦幻或冰冷的角色"},
        ]
        return data

    @staticmethod  # 发型
    def HairStyle():
        data = [
            {"key":"长发", "value":"long", "description":"长而顺直的头发，带有优雅、温柔的气质，适合高贵或柔美的角色形象"},
            {"key":"短发", "value":"short", "description":"较短的头发，干练而清爽，适合塑造活泼、现代或独立的角色"},
            {"key":"卷发", "value":"curly", "description":"自然的卷曲发型，充满动感和个性，适合热情或随性的角色"},
            {"key":"直发", "value":"straight", "description":"顺直的头发，柔顺整齐，适合塑造端庄、冷静或高雅的角色形象"},
            {"key":"波浪卷", "value":"wavy", "description":"轻柔的波浪卷发，增添了柔和和浪漫的气质，适合温柔或充满魅力的角色"},
            {"key":"马尾", "value":"ponytail", "description":"高高扎起的马尾，青春活力，适合塑造运动型或元气满满的角色"},
            {"key":"双马尾", "value":"pigtails", "description":"左右两侧扎起的马尾，显得俏皮可爱，适合活泼、年轻的角色形象"},
            {"key":"编发", "value":"braids", "description":"编织成辫子的发型，给人一种民族、传统或精致的感觉"},
            {"key":"高马尾", "value":"high ponytail", "description":"高高扎起的马尾，干练且充满自信，适合坚强或活力型角色"},
            {"key":"低马尾", "value":"low ponytail", "description":"低垂的马尾，显得温柔且优雅，适合成熟、稳重的角色"},
            {"key":"短卷发", "value":"short curly", "description":"短发卷曲，带有俏皮的氛围，适合表现开朗、个性的角色"},
            {"key":"侧边辫", "value":"side braid", "description":"一侧的辫子，富有异域风情，适合温柔或田园风格的角色"},
            {"key":"盘发", "value":"bun", "description":"头发盘成圆形，显得整洁而优雅，适合正式、端庄的角色"},
            {"key":"丸子头", "value":"top bun", "description":"高高的丸子头，休闲且俏皮，适合轻松、可爱的形象"},
            {"key":"发髻", "value":"chignon", "description":"低盘的发髻，显得优雅且古典，适合成熟、优雅的角色"},
            {"key":"卷边短发", "value":"bob cut", "description":"齐耳短发带卷，带有现代感，适合干练、独立的角色"},
            {"key":"鬓角编发", "value":"side cornrows", "description":"在鬓角编织的发辫，带有独特的风格，适合前卫、时尚的形象"},
            {"key":"长卷发", "value":"long curly", "description":"长而卷曲的头发，充满柔美的气质，适合塑造充满魅力的角色"},
            {"key":"长直发", "value":"long straight", "description":"长而顺直的头发，温柔且优雅，适合经典、美丽的形象"},
            {"key":"爆炸头", "value":"afro", "description":"蓬松的爆炸卷发，独特且充满个性，适合表现自由、独特的形象"},
            {"key":"寸头", "value":"buzz cut", "description":"极短的寸头，干练且简洁，适合勇敢或个性的角色"},
            {"key":"中分直发", "value":"middle part straight", "description":"中分的直发，简洁自然，适合塑造柔和、端庄的形象"},
            {"key":"侧分卷发", "value":"side part wavy", "description":"侧分的波浪卷发，带有成熟的韵味，适合时尚或优雅的角色"},
        ]
        return data

    @staticmethod
    def RandomDescription():
        gender = random.choice(AppearanceDescription.Gender())["value"]
        body_type = random.choice(AppearanceDescription.BodyType())["value"]
        skin_tone = random.choice(AppearanceDescription.SkinTone())["value"]
        regional = random.choice(AppearanceDescription.Regional())["value"]
        hair_color = random.choice(AppearanceDescription.HairColor())["value"]
        hair_style = random.choice(AppearanceDescription.HairStyle())["value"]

        return AppearanceDescription.BasePrompt(gender, body_type, skin_tone, regional, hair_style, hair_color)

