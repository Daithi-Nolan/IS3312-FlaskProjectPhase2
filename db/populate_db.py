from db.extensions import db
from app import app
from model.models import User, Product


def seed_database():
    with app.app_context():
        db.session.query(Product).delete()  # Delete all existing products
        db.session.query(User).delete()  # Delete all exiting users
        db.session.commit()

        # Add Initial Products
        products = [

            # North America
            Product(id="WW001", name="Bears Ahead (USA)", brand="HSD", price=100.00, coating="Diamond-Grade Sheeting",
                    materials="Heavy-Gauge Marine-Grade Aluminum (5052-H38 Alloy)",
                    embossing="Laser-Cut Raised Aluminum",
                    image_url="images/american/bears_ahead.svg",
                    description="The Bears Ahead sign is an essential warning for drivers in areas prone to wildlife crossings. This sign, made from durable materials, ensures visibility in all weather conditions and alerts drivers to the potential presence of bears. Perfect for rural regions or wildlife reserves, it provides an important safety measure for both animals and motorists, helping to reduce unexpected encounters.",
                    country="North America"),
            Product(id="WW002", name="Interstate-95 Sign (USA)", brand="PWS Signs", price=115.00,
                    coating="High Intensity Prismatic (HIP)",
                    materials="Galvanized Carbon Steel", embossing="Indented Steel Embossing",
                    image_url="images/american/i_95.svg",
                    description="The I-95 road sign marks one of the major highways on the East Coast of the United States. Constructed from high-quality galvanized steel, it features prismatic sheeting for enhanced visibility. Designed for use along the entire length of Interstate 95, this sign is crucial for guiding drivers through states, helping ensure safety and easy navigation over long distances.",
                    country="North America"),
            Product(id="WW003", name="Pedestrian Crossing (Canada)", brand="Ernco Group", price=127.00,
                    coating="Standard Engineering Grade",
                    materials="Powder-Coated Aluminum (6061-T6 Alloy)", embossing="Machine-Pressed Hybrid",
                    image_url="images/american/pedestrian_crossing.svg",
                    description="The Pedestrian Crossing sign serves as a vital alert for drivers to be cautious of pedestrians in designated areas. Its bright color and clear markings are designed to catch the eye, reducing the risk of accidents. Manufactured from durable, weather-resistant materials, this sign is ideal for busy intersections, schools, and community areas, emphasizing safety for all road users.",
                    country="North America"),
            Product(id="WW004", name="Route 34 Sign (USA)", brand="HSD", price=110.00, coating="Diamond-Grade Sheeting",
                    materials="Heavy-Gauge Marine-Grade Aluminum (5052-H38 Alloy)",
                    embossing="Laser-Cut Raised Aluminum",
                    image_url="images/american/route_34.svg",
                    description="The Route 34 sign is a key identifier for this popular highway. Made from heavy-gauge aluminum with laser-cut raised embossing, it provides durability and high visibility. Route signs help motorists navigate efficiently and maintain a safe journey. The reflective coating enhances night-time visibility, making it a reliable and essential road sign for drivers across all conditions.",
                    country="North America"),

            # Europe
            Product(id="WW005", name="Roundabout Sign (EU)", brand="Ernco Group", price=125.00,
                    coating="Standard Engineering Grade",
                    materials="Powder-Coated Aluminum (6061-T6 Alloy)", embossing="Machine-Pressed Hybrid",
                    image_url="images/european/roundabout.svg",
                    description="The Roundabout sign is used to warn drivers of an approaching roundabout junction. This durable sign is crafted from powder-coated aluminum, offering resistance to corrosion and ensuring longevity. The clear roundabout symbol helps reduce confusion among drivers, contributing to smoother traffic flow and preventing accidents at intersections. It is particularly crucial in urban and suburban areas where roundabouts are common.",
                    country="Europe"),
            Product(id="WW006", name="Speed Limit 50km/h (Ireland)", brand="PWS Signs", price=140.00,
                    coating="High Intensity Prismatic (HIP)",
                    materials="Galvanized Carbon Steel", embossing="Indented Steel Embossing",
                    image_url="images/european/speed_limit_50.svg",
                    description="The Speed Limit 50 sign is essential for maintaining safe driving speeds in urban areas. Built using galvanized carbon steel, this sign is both durable and highly reflective. Its prismatic coating ensures maximum visibility, even in low-light conditions, reminding drivers to keep within the speed limits to enhance road safety, reduce accidents, and comply with traffic regulations.",
                    country="Europe"),
            Product(id="WW007", name="Stop Sign (UK & Ireland)", brand="HSD", price=150.00,
                    coating="Diamond-Grade Sheeting",
                    materials="Heavy-Gauge Marine-Grade Aluminum (5052-H38 Alloy)",
                    embossing="Laser-Cut Raised Aluminum",
                    image_url="images/european/stop.svg",
                    description="The Stop sign is one of the most recognizable and important road signs globally. Manufactured with high-quality diamond-grade sheeting, it ensures drivers are alerted to come to a complete stop at intersections. This sign is designed to withstand adverse weather conditions, providing a critical reminder for safety at junctions and crossings to prevent accidents and protect pedestrians.",
                    country="Europe"),
            Product(id="WW008", name="Traffic Light Sign (UK & Ireland)", brand="Ernco Group", price=132.00,
                    coating="High Intensity Prismatic (HIP)",
                    materials="Powder-Coated Aluminum (6061-T6 Alloy)", embossing="Machine-Pressed Hybrid",
                    image_url="images/european/traffic_light.svg",
                    description="The Traffic Light sign serves as an advance warning for upcoming traffic signal lights, helping drivers prepare for potential stops. It is built with high-intensity prismatic sheeting, which enhances its visibility from a distance. Suitable for urban roads, the reflective coating ensures it remains visible in both daytime and nighttime conditions, significantly improving driver awareness.",
                    country="Europe"),

            # Japan
            Product(id="WW009", name="Junction Sign (Japan)", brand="HSD", price=185.00,
                    coating="Diamond-Grade Sheeting",
                    materials="Heavy-Gauge Marine-Grade Aluminum (5052-H38 Alloy)",
                    embossing="Laser-Cut Raised Aluminum",
                    image_url="images/japanese/jap_junction.svg",
                    description="The Japanese Junction Sign is crucial for indicating complex junctions ahead, common in urban environments. This sign features high-quality diamond-grade sheeting for maximum reflectivity and visibility. Constructed from marine-grade aluminum, it resists rust and degradation, ensuring longevity. It helps drivers anticipate upcoming turns and prepare for intersections, thus contributing to smoother and safer traffic flow.",
                    country="Japan"),
            Product(id="WW010", name="Slow Sign (Japan)", brand="PWS Signs", price=170.00,
                    coating="High Intensity Prismatic (HIP)",
                    materials="Galvanized Carbon Steel", embossing="Indented Steel Embossing",
                    image_url="images/japanese/jap_slow.svg",
                    description="The Japanese Slow Sign advises drivers to reduce speed in designated areas, such as school zones or pedestrian crossings. Made from high-intensity prismatic materials, it ensures visibility from a distance. The robust design, crafted from galvanized steel, is resistant to harsh weather conditions, making it a durable and essential part of traffic safety infrastructure.",
                    country="Japan"),
            Product(id="WW011", name="Speed Limit 60km/h (Japan)", brand="Ernco Group", price=199.00,
                    coating="Standard Engineering Grade",
                    materials="Powder-Coated Aluminum (6061-T6 Alloy)", embossing="Machine-Pressed Hybrid",
                    image_url="images/japanese/jap_speed_limit_60.svg",
                    description="The Japanese Speed Limit 60km/h sign ensures drivers maintain a safe speed on certain road sections. Its reflective engineering-grade coating guarantees visibility under headlights, while the durable aluminum construction withstands Japan's diverse weather conditions. This sign is especially important on highways and main roads to promote orderly traffic movement and prevent speeding.",
                    country="Japan"),
            Product(id="WW012", name="Stop Sign (Japan)", brand="HSD", price=210.00, coating="Diamond-Grade Sheeting",
                    materials="Heavy-Gauge Marine-Grade Aluminum (5052-H38 Alloy)",
                    embossing="Laser-Cut Raised Aluminum",
                    image_url="images/japanese/jap_stop.svg",
                    description="The Japanese Stop Sign is designed to clearly signal drivers to come to a complete stop before proceeding. Its diamond-grade reflective coating ensures high visibility, day or night, and the sturdy aluminum build guarantees durability. This sign plays an essential role in maintaining safe driving practices, particularly at intersections, by preventing potential collisions.",
                    country="Japan")
        ]
        db.session.bulk_save_objects(products)  # ✅ Bulk insert for performance

        # Add Admin User - PyCharm flags these as an unexpected arguments, but it works fine
        admin_user = User(
            username="admin",
            first_name="Admin",
            last_name="User",
            email="admin@weatherway.com",
            role="admin"
        )
        admin_user.set_password("Admin123!")  # Securely hash password

        db.session.add(admin_user)
        db.session.commit()

        print("✅ Database seeded with initial data (Products & Admin User).")
        print(User)


if __name__ == "__main__":
    seed_database()
