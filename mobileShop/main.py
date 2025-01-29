from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import phones_db, brands_db, laptops_db
from datetime import datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")






@app.get("/")
async def home(request: Request):
    featured_phones = [phone for phone in phones_db if phone["featured"]]
    featured_laptops = [laptop for laptop in laptops_db if laptop["featured"]]

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "featured_phones": featured_phones,
            "featured_laptops": featured_laptops,
            "brands": brands_db,
        }
    )


@app.get("/brand/{brand_id}")
async def brand_products(request: Request, brand_id: str):
    brand = next((b for b in brands_db if b["id"] == brand_id), None)
    brand_phones = [phone for phone in phones_db if phone["brand_id"] == brand_id]
    brand_laptops = [laptop for laptop in laptops_db if laptop["brand_id"] == brand_id]

    return templates.TemplateResponse(
        "brand_products.html",  # Renamed template to reflect both phones & laptops
        {
            "request": request,
            "brand": brand,
            "phones": brand_phones,
            "laptops": brand_laptops,
        }
    )





@app.get("/phone/{phone_id}")
async def phone_detail(request: Request, phone_id: str):
    phone = next((p for p in phones_db if p["id"] == phone_id), None)
    return templates.TemplateResponse(
        "phone_details.html",
        {"request": request, "phone": phone}
    )


#laptops details page
@app.get("/laptop/{laptop_id}")
async def laptop_detail(request: Request, laptop_id: str):
    laptop = next((l for l in laptops_db if l["id"] == laptop_id), None)
    return templates.TemplateResponse(
        "laptop_details.html",
        {"request": request, "laptop": laptop}
    )



#phones page
@app.get("/phones")
async def phones(request: Request):
    return templates.TemplateResponse(
        "phones.html",
        {"request": request, "phones": phones_db}
    )


#laptops page
@app.get("/laptops")
async def phones(request: Request):
    return templates.TemplateResponse(
        "laptops.html",
        {"request": request, "laptops": laptops_db}
    )


@app.get("/contact")
async def phones(request: Request):
    return templates.TemplateResponse(
        "contact.html",
        {"request": request, "laptops": laptops_db}
    )



@app.get("/about")
async def phones(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {"request": request, "laptops": laptops_db}
    )


@app.get("/privacy")
async def phones(request: Request):
    return templates.TemplateResponse(
        "privacy.html",
        {"request": request, "laptops": laptops_db}
    )





#Sitemap:::::::::::::::::::::
@app.get("/sitemap.xml")
async def sitemap():

    # Construct the XML structure
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    XML_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"
    xml_content += f'<urlset xmlns="{XML_NAMESPACE}">\n'

    base_url = "https://mobileshop.com"
    xml_content += f"""
        <loc>{base_url}</loc>
    """

    urls = []
    for brand in brands_db:
        urls.append(f"{base_url}/brand/{brand['id']}")

    for phone in phones_db:
        urls.append(f"{base_url}/phone/{phone['id']}")


    for url in urls:
        xml_content += "  <url>\n"
        xml_content += f"    <loc>{url}</loc>\n"
        xml_content += f"    <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>\n"
        xml_content += f"    <changefreq>weekly</changefreq>\n"
        xml_content += f"    <priority>1</priority>\n"
        xml_content += "  </url>\n"

    xml_content += "</urlset>"

    return Response(content=xml_content, media_type="application/xml")









#Robots file:::::::::::::::::::
@app.get("/robots.txt")
async def robot():
    content = """"
        user-agent: *
        Allow: /
        Disallow: /admin
        Sitemap: https://mobileshop.com/sitemap.xml
    """
    return Response(content = content)




