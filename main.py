from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Brew DB API",
    description="Coffee drinks from around the world",
    version="1.0.0"
)

# CORS middleware to allow from 3000 & vercel app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://your-vercel-app.vercel.app"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)

# why we add pydantic - validate data and create a model(schema) response for API, access fields as attributes, not plain dict keys
class Brew(BaseModel):
    name: str
    origin: str
    roast: str
    image: str
    taste_profile: List[str]

# sample data
brews: List[Brew] = [
    Brew(name="Turkish Coffee", origin="Turkey", roast="Medium", taste_profile=["Acidic", "Bitter"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Turkish_coffee_Turk_kahvesi.jpg/960px-Turkish_coffee_Turk_kahvesi.jpg"),
    Brew(name="Frappé", origin="Greece", roast="Medium", taste_profile=["Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Frapp%C3%A9.jpg/960px-Frapp%C3%A9.jpg"),
    Brew(name="Caffè Macchiato", origin="Italy", roast="Dark", taste_profile=["Bitter", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Macchiato_FourBarrel.jpg/960px-Macchiato_FourBarrel.jpg"),
    Brew(name="Ca Phe Sua Da", origin="Vietnam", roast="Dark, Medium", taste_profile=["Bitter", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Viet-coffee.jpg/960px-Viet-coffee.jpg"),
    Brew(name="Caffè Mocha", origin="Yemen", roast="Dark, Medium", taste_profile=["Chocolate", "Nutty", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Mocha_-_Si_Signore_2024-01-15.jpg/960px-Mocha_-_Si_Signore_2024-01-15.jpg"),
    Brew(name="Café Bombón", origin="Spain", roast="Medium", taste_profile=["Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Caf%C3%A9s_bomb%C3%B3n_-_Burgos.jpg/960px-Caf%C3%A9s_bomb%C3%B3n_-_Burgos.jpg"),
    Brew(name="Cappuccino", origin="Italy", roast="Light, Medium", taste_profile=["Acidic", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/A_cup_of_cappuccino.jpg/960px-A_cup_of_cappuccino.jpg"),
    Brew(name="Café Cubano", origin="Cuba", roast="Dark", taste_profile=["Acidic", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Cafe_cubano_de_la_marca_Cubita_Gourmet.JPG/960px-Cafe_cubano_de_la_marca_Cubita_Gourmet.JPG"),
    Brew(name="Caffè Corretto", origin="Italy", roast="Dark, Medium", taste_profile=["Bitter", "Fruity"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Caff%C3%A8_corretto.jpg/960px-Caff%C3%A8_corretto.jpg"),
    Brew(name="Oliang", origin="Thailand", roast="Dark", taste_profile=["Bitter", "Earthy", "Nutty", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Oliang_%E0%B9%82%E0%B8%AD%E0%B9%80%E0%B8%A5%E0%B8%B5%E0%B9%89%E0%B8%A2%E0%B8%87_oleang_olieng_Thai_iced_coffee_at_Ayutthaya.jpg/960px-Oliang_%E0%B9%82%E0%B8%AD%E0%B9%80%E0%B8%A5%E0%B8%B5%E0%B9%89%E0%B8%A2%E0%B8%87_oleang_olieng_Thai_iced_coffee_at_Ayutthaya.jpg"),
    Brew(name="Einspänner", origin="Austria", roast="Dark", taste_profile=["Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Einsp%C3%A4nner_Kaffee.jpg/960px-Einsp%C3%A4nner_Kaffee.jpg"),
    Brew(name="Dalgona Coffee", origin="China", roast="Medium", taste_profile=["Caramel", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Dalgona_coffee.jpg/960px-Dalgona_coffee.jpg"),
    Brew(name="Kaffeost", origin="Sweden", roast="Dark", taste_profile=["Acidic", "Bitter"], image="https://cdn.shopify.com/s/files/1/0240/4653/4736/files/4_edb2980d-670d-49d0-bf1f-e1e68ecb1e8a_480x480.jpg?v=1686217751"),
    Brew(name="Café de Olla", origin="Mexico", roast="Dark, Medium", taste_profile=["Bitter", "Earthy", "Spicy", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Caf%C3%A9_de_Olla_y_pan_de_pueblo.jpg/960px-Caf%C3%A9_de_Olla_y_pan_de_pueblo.jpg"),
    Brew(name="Yuenyeung", origin="Hong Kong", roast="Medium", taste_profile=["Acidic", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Yuanyang_%28drink%29.jpg/960px-Yuanyang_%28drink%29.jpg"),
    Brew(name="Café au Lait", origin="France", roast="Medium", taste_profile=["Acidic", "Bitter"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Caf%C3%A9_au_lait.jpg/960px-Caf%C3%A9_au_lait.jpg"),
    Brew(name="Irish Coffee", origin="Ireland", roast="Dark, Medium", taste_profile=["Acidic", "Earthy"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Irish_Coffee.jpg/960px-Irish_Coffee.jpg"),
    Brew(name="Indian Filter Coffee", origin="India", roast="Dark", taste_profile=["Acidic", "Bitter", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Filter-Coffee.jpg/960px-Filter-Coffee.jpg"),
    Brew(name="Kopi Luwak", origin="Indonesia", roast="Dark, Light", taste_profile=["Smoky"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Kopi_Bukit_Luncuk_Danau_Ranau.jpg/960px-Kopi_Bukit_Luncuk_Danau_Ranau.jpg"),
    Brew(name="Affogato", origin="Italy", roast="Medium", taste_profile=["Floral", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Vinoteca%2C_Smithfield%2C_London_%284485849609%29.jpg/960px-Vinoteca%2C_Smithfield%2C_London_%284485849609%29.jpg"),
    Brew(name="Mazagran", origin="Algeria", roast="Dark, Medium", taste_profile=["Acidic", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Caf%C3%A9_mazagran.jpg/960px-Caf%C3%A9_mazagran.jpg"),
    Brew(name="Café Touba", origin="Senegal", roast="Medium", taste_profile=["Acidic", "Bitter", "Spicy"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Caf%C3%A9_Touba._Pouring.jpg/960px-Caf%C3%A9_Touba._Pouring.jpg"),
    Brew(name="Bicerin", origin="Italy", roast="Dark", taste_profile=["Bitter", "Chocolate", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Bicerin.jpg/960px-Bicerin.jpg"),
    Brew(name="Flat White", origin="Australia", roast="Light, Medium", taste_profile=["Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Flat_White_1.jpg/960px-Flat_White_1.jpg"),
    Brew(name="Latte", origin="Italy", roast="Light", taste_profile=["Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Caff%C3%A8_latte.jpg/960px-Caff%C3%A8_latte.jpg"),
    Brew(name="Cortado", origin="Spain", roast="Medium", taste_profile=["Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Cortado_-_Vios_2024-01-09.jpg/960px-Cortado_-_Vios_2024-01-09.jpg"),
    Brew(name="Espresso", origin="Italy", roast="Dark, Medium", taste_profile=["Acidic", "Bitter"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/A_cup_of_espresso.jpg/960px-A_cup_of_espresso.jpg"),
    Brew(name="Qahwa", origin="Yemen", roast="Light", taste_profile=["Acidic", "Spicy", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Arabic_coffee_with_dates.jpg/960px-Arabic_coffee_with_dates.jpg"),
    Brew(name="Galão", origin="Portugal", roast="Medium", taste_profile=["Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Gal%C3%A3o.jpg/960px-Gal%C3%A3o.jpg"),
    Brew(name="Matcha Latte", origin="Unknown", roast="None", taste_profile=["Earthy", "Floral", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Matcha_tea_latte_with_rosetta_latte_art.jpg/960px-Matcha_tea_latte_with_rosetta_latte_art.jpg"),
    Brew(name="Butterfly Pea Latte", origin="Unknown", roast="None", taste_profile=["Floral", "Fruity", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Butterfly_Latte_-_Keys_%26_Co._2025-03-27.jpg/960px-Butterfly_Latte_-_Keys_%26_Co._2025-03-27.jpg"),
    Brew(name="Pumpkin Spice Latte", origin="Unknown", roast="None", taste_profile=["Earthy", "Spicy", "Sweet"], image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Pumpkin_Spice_%2848986157673%29_cropped.png/960px-Pumpkin_Spice_%2848986157673%29_cropped.png"),
]

# root endpoint
@app.get("/")
def root():
    return {"message": "☕ Welcome to Brew DB API"}

# get coffee brews simple list
# @app.get("/brews")
# def get_all_brews():
#     return {"total": len(brews), "brews": brews}

# get coffee brews with query parameters
@app.get("/brews", response_model=List[Brew])
def get_all_brews(roast: Optional[str] = None, taste: Optional[str] = None):
    results = brews

    if roast:
        results = [b for b in results if b.roast.lower() == roast.lower()]

    if taste:
        results = [b for b in results if taste.lower() in [t.lower() for t in b.taste_profile]]

    return results

# single coffee brew fetch
@app.get("/brews/{name}", response_model=Brew)
def get_brew_by_name(name: str):
    for brew in brews:
        if brew.name.lower() == name.lower():
            return brew
    raise HTTPException(status_code=404, detail=f"Coffee '{name}' not found")

# add a new brew
@app.post("/brews", response_model=Brew)
def add_brew(brew: Brew):
    for existing in brews:
        if existing.name.lower() == brew.name.lower():
            raise HTTPException(status_code=400, detail=f"Brew '{brew.name}' already exists")
    brews.append(brew)
    return brew