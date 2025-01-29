brands_db = [
    {"id": "samsung", "name": "Samsung", "logo": "samsung-logo.png"},
    {"id": "apple", "name": "Apple", "logo": "apple-logo.png"},
    {"id": "xiaomi", "name": "Xiaomi", "logo": "xiaomi-logo.png"},
    {"id": "oneplus", "name": "OnePlus", "logo": "oneplus-logo.png"},
    {"id": "google", "name": "Google", "logo": "google-logo.png"},
    
    # Laptop brands
    {"id": "dell", "name": "Dell", "logo": "dell-logo.png"},
    {"id": "hp", "name": "HP", "logo": "hp-logo.png"},
    {"id": "lenovo", "name": "Lenovo", "logo": "lenovo-logo.png"},
    {"id": "asus", "name": "Asus", "logo": "asus-logo.png"},
    {"id": "acer", "name": "Acer", "logo": "acer-logo.png"}
]

phones_db = [
    {
        "id": "samsung-s24-ultra",
        "brand_id": "samsung",
        "name": "Samsung Galaxy S24 Ultra",
        "price": 1299.99,
        "featured": True,
        "image": "s24-ultra.jpg",
        "specs": {
            "display": "6.8-inch Dynamic AMOLED 2X",
            "processor": "Snapdragon 8 Gen 3",
            "ram": "12GB",
            "storage": "256GB/512GB/1TB",
            "camera": "200MP + 12MP + 10MP + 10MP",
            "battery": "5000mAh"
        }
    },
    {
        "id": "apple-iphone-15-pro",
        "brand_id": "apple",
        "name": "Apple iPhone 15 Pro",
        "price": 1199.99,
        "featured": True,
        "image": "iphone-15-pro.jpg",
        "specs": {
            "display": "6.1-inch Super Retina XDR",
            "processor": "A17 Bionic",
            "ram": "8GB",
            "storage": "128GB/256GB/512GB/1TB",
            "camera": "48MP + 12MP",
            "battery": "3200mAh"
        }
    },
    {
        "id": "xiaomi-mi-13-ultra",
        "brand_id": "xiaomi",
        "name": "Xiaomi Mi 13 Ultra",
        "price": 1099.99,
        "featured": False,
        "image": "mi-13-ultra.jpg",
        "specs": {
            "display": "6.73-inch LTPO AMOLED",
            "processor": "Snapdragon 8 Gen 2",
            "ram": "12GB",
            "storage": "256GB/512GB/1TB",
            "camera": "50MP + 50MP + 50MP + 50MP",
            "battery": "5000mAh"
        }
    },
    {
        "id": "oneplus-12",
        "brand_id": "oneplus",
        "name": "OnePlus 12",
        "price": 899.99,
        "featured": True,
        "image": "oneplus-12.jpg",
        "specs": {
            "display": "6.7-inch AMOLED",
            "processor": "Snapdragon 8 Gen 3",
            "ram": "16GB",
            "storage": "256GB/512GB",
            "camera": "50MP + 50MP + 64MP",
            "battery": "5400mAh"
        }
    },
    {
        "id": "google-pixel-8-pro",
        "brand_id": "google",
        "name": "Google Pixel 8 Pro",
        "price": 999.99,
        "featured": False,
        "image": "pixel-8-pro.jpg",
        "specs": {
            "display": "6.7-inch LTPO OLED",
            "processor": "Tensor G3",
            "ram": "12GB",
            "storage": "128GB/256GB/512GB",
            "camera": "50MP + 48MP + 48MP",
            "battery": "5050mAh"
        }
    },
    {
        "id": "google-pixel-8-pro",
        "brand_id": "google",
        "name": "Google Pixel 8 Pro",
        "price": 999.99,
        "featured": False,
        "image": "pixel-8-pro.jpg",
        "specs": {
            "display": "6.7-inch LTPO OLED",
            "processor": "Tensor G3",
            "ram": "12GB",
            "storage": "128GB/256GB/512GB",
            "camera": "50MP + 48MP + 48MP",
            "battery": "5050mAh"
        }
    },
    {
        "id": "google-pixel-8-pro",
        "brand_id": "google",
        "name": "Google Pixel 8 Pro",
        "price": 999.99,
        "featured": False,
        "image": "pixel-8-pro.jpg",
        "specs": {
            "display": "6.7-inch LTPO OLED",
            "processor": "Tensor G3",
            "ram": "12GB",
            "storage": "128GB/256GB/512GB",
            "camera": "50MP + 48MP + 48MP",
            "battery": "5050mAh"
        }
    },
    {
        "id": "google-pixel-8-pro",
        "brand_id": "google",
        "name": "Google Pixel 8 Pro",
        "price": 999.99,
        "featured": False,
        "image": "pixel-8-pro.jpg",
        "specs": {
            "display": "6.7-inch LTPO OLED",
            "processor": "Tensor G3",
            "ram": "12GB",
            "storage": "128GB/256GB/512GB",
            "camera": "50MP + 48MP + 48MP",
            "battery": "5050mAh"
        }
    }
]



laptops_db = [
    {
        "id": "macbook-pro-16-m3",
        "brand_id": "apple",
        "name": "MacBook Pro 16 (M3)",
        "price": 2499.99,
        "featured": True,
        "image": "https://images.pexels.com/photos/205421/pexels-photo-205421.jpeg?cs=srgb&dl=pexels-craigmdennis-205421.jpg&fm=jpg",
        "specs": {
            "display": "16.2-inch Liquid Retina XDR",
            "processor": "Apple M3 Pro",
            "ram": "16GB/32GB/64GB",
            "storage": "512GB/1TB/2TB/4TB/8TB",
            "battery": "22 hours"
        }
    },
    {
        "id": "dell-xps-15-9530",
        "brand_id": "dell",
        "name": "Dell XPS 15 (9530)",
        "price": 1999.99,
        "featured": True,
        "image": "https://images.pexels.com/photos/205421/pexels-photo-205421.jpeg?cs=srgb&dl=pexels-craigmdennis-205421.jpg&fm=jpg",
        "specs": {
            "display": "15.6-inch 3.5K OLED",
            "processor": "Intel Core i7-13700H",
            "ram": "16GB/32GB/64GB",
            "storage": "512GB/1TB/2TB/4TB",
            "battery": "86Wh"
        }
    },
    {
        "id": "asus-rog-zephyrus-g14",
        "brand_id": "asus",
        "name": "Asus ROG Zephyrus G14",
        "price": 1899.99,
        "featured": False,
        "image": "https://images.pexels.com/photos/205421/pexels-photo-205421.jpeg?cs=srgb&dl=pexels-craigmdennis-205421.jpg&fm=jpg",
        "specs": {
            "display": "14-inch Mini LED 165Hz",
            "processor": "AMD Ryzen 9 7940HS",
            "ram": "16GB/32GB/64GB",
            "storage": "1TB/2TB",
            "battery": "76Wh"
        }
    },
    {
        "id": "lenovo-legion-7i",
        "brand_id": "lenovo",
        "name": "Lenovo Legion 7i",
        "price": 2199.99,
        "featured": True,
        "image": "https://images.pexels.com/photos/205421/pexels-photo-205421.jpeg?cs=srgb&dl=pexels-craigmdennis-205421.jpg&fm=jpg",
        "specs": {
            "display": "16-inch WQXGA 240Hz",
            "processor": "Intel Core i9-13900HX",
            "ram": "16GB/32GB/64GB",
            "storage": "512GB/1TB/2TB",
            "battery": "99.9Wh"
        }
    },
    {
        "id": "hp-spectre-x360-14",
        "brand_id": "hp",
        "name": "HP Spectre x360 14",
        "price": 1799.99,
        "featured": False,
        "image": "https://images.pexels.com/photos/205421/pexels-photo-205421.jpeg?cs=srgb&dl=pexels-craigmdennis-205421.jpg&fm=jpg",
        "specs": {
            "display": "13.5-inch OLED 3K",
            "processor": "Intel Core i7-1365U",
            "ram": "16GB/32GB",
            "storage": "512GB/1TB/2TB",
            "battery": "66Wh"
        }
    },
    {
        "id": "acer",
        "brand_id": "acer",
        "name": "Acer Spectre x360 14",
        "price": 1 ,
        "featured": False,
        "image": "https://images.pexels.com/photos/205421/pexels-photo-205421.jpeg?cs=srgb&dl=pexels-craigmdennis-205421.jpg&fm=jpg",
        "specs": {
            "display": "13.5-inch OLED 3K",
            "processor": "Intel Core i7-1365U",
            "ram": "16GB/32GB",
            "storage": "512GB/1TB/2TB",
            "battery": "66Wh"
        }
    },
    {
        "id": "acer",
        "brand_id": "acer",
        "name": "Acer Spectre x360 14",
        "price": 1 ,
        "featured": False,
        "image": "https://images.pexels.com/photos/205421/pexels-photo-205421.jpeg?cs=srgb&dl=pexels-craigmdennis-205421.jpg&fm=jpg",
        "specs": {
            "display": "13.5-inch OLED 3K",
            "processor": "Intel Core i7-1365U",
            "ram": "16GB/32GB",
            "storage": "512GB/1TB/2TB",
            "battery": "66Wh"
        }
    },
    {
        "id": "acer",
        "brand_id": "acer",
        "name": "Acer Spectre x360 14",
        "price": 1 ,
        "featured": False,
        "image": "https://images.pexels.com/photos/205421/pexels-photo-205421.jpeg?cs=srgb&dl=pexels-craigmdennis-205421.jpg&fm=jpg",
        "specs": {
            "display": "13.5-inch OLED 3K",
            "processor": "Intel Core i7-1365U",
            "ram": "16GB/32GB",
            "storage": "512GB/1TB/2TB",
            "battery": "66Wh"
        }
    }
]



featured_phones = [
    {
        "id": "samsung-s24-ultra",
        "name": "Samsung Galaxy S24 Ultra",
        "price": 1299.99,
        "image": "https://images-cdn.ubuy.co.in/65f583b532f0c2533936d279-samsung-galaxy-s24-ultra-cell-phone.jpg"
    },
    {
        "id": "apple-iphone-15-pro",
        "name": "Apple iPhone 15 Pro",
        "price": 1199.99,
        "image": "https://rukminim2.flixcart.com/image/850/1000/xif0q/mobile/h/d/9/-original-imagtc2qzgnnuhxh.jpeg?q=90&crop=false"
    },
    {
        "id": "xiaomi-mi-13-ultra",
        "name": "Xiaomi Mi 13 Ultra",
        "price": 1099.99,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyIWfHBdwiwzzwjZ9ELp-4r2d8wISx8G65rA&s"
    },
    {
        "id": "oneplus-12",
        "name": "OnePlus 12",
        "price": 899.99,
        "image": "https://m.media-amazon.com/images/I/61AplC-qoML._AC_UF350,350_QL80_.jpg"
    },
    {
        "id": "google-pixel-8-pro",
        "name": "Google Pixel 8 Pro",
        "price": 999.99,
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdBucE0biNLEUPSOyikuWB-dAJNNql5_jeQg&s"
    },
    {
        "id": "samsung-a54",
        "name": "Samsung Galaxy A54",
        "price": 449.99,
        "image": "https://images-cdn.ubuy.co.in/6536416aec5d2f148e3dc1e4-samsung-galaxy-a54-5g-a-series-cell.jpg"
    },
    {
        "id": "apple-iphone-se-3",
        "name": "Apple iPhone SE 3",
        "price": 429.99,
        "image": "https://images-cdn.ubuy.co.in/65b55b81e666591b1735fcc6-refurbished-apple-iphone-se-3rd-gen.jpg"
    }
]
