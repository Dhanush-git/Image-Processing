from PIL import Image , ImageDraw , ImageFont
from io import BytesIO
import requests

def Image_process(USER_NAME,USER_PFP_URL,CUR_XP,MAX_XP):
        
    bg = Image.new('RGBA',(600,200),'#7289DA')

    PROGRESS_CORD = int((400*CUR_XP)/MAX_XP)
    

    pfp = Image.open(requests.get(USER_PFP_URL, stream=True).raw).resize((130,130)).convert('RGBA')
    pfp_mask = Image.open('img/pfp_mask.png').resize((130,130)).convert('L')


    progress_bar = Image.new('RGBA',(400,30),'#434343')
    progress_bar_mask = Image.open('img/progress_mask.png').resize((400,30)).convert('L')
    progress_bar_fill = Image.new('RGBA',(PROGRESS_CORD,30),'#FFFFFF')

    progress_bar.paste(progress_bar_fill,(0,0))

    bg.paste(pfp,(29,35),pfp_mask)
    bg.paste(progress_bar,(177,129),progress_bar_mask)

    draw = ImageDraw.Draw(bg)

    font_name = ImageFont.truetype(r'fonts/font.ttf', 20)
    font_xp = ImageFont.truetype(r'fonts/font.ttf', 15)

    draw.text((191,101),USER_NAME,align='left',font=font_name, fill='#FFFFFF')
    draw.text((502,106),f'{CUR_XP}/{MAX_XP}',align='left',font=font_xp, fill='#FFFFFF')

    byteImgIO = BytesIO()
    byteImg = bg
    byteImg.save(byteImgIO, "PNG")
    byteImgIO.seek(0)
    byteImg = byteImgIO.read()

    with Image.open(BytesIO(byteImg)) as my_image:

            output_buffer = BytesIO()
            my_image.save(output_buffer, "png")
            output_buffer.seek(0)
            


            return(output_buffer)