import requests

url = "http://127.0.0.1:5000"

response = requests.get(url)
from bson import ObjectId

# service_name = "openai"
# model_name = "gpt-4.1"
# user_id = "68e553454e05fbc189605af0"
# api_key = ""
# topic_name = "Sample AI Test"
# topic_description = "You are an helpful AI"
# tools = "code_interpreter,web_search"
#
# service = requests.post(url + "/api/service", json={"service_name": service_name, "user_id": user_id, "api_key": api_key})
# agent = requests.post(url + "/api/agent", json={"service_id": service.json()["id"], "model_name": model_name})
# topic = requests.post(url + "/api/topic", json={"agent_id": agent.json()["id"], "topic_name": topic_name, "topic_description": topic_description, "tools": tools})
# context = requests.post(url + "/api/context", json={})
#
#
# thread = requests.post(url + "/api/thread", json={"topic_id": topic.json()["id"], "context_id": context.json()["id"]})
# thread_id = thread.json()["id"]

user_id = "68e553454e05fbc189605ah0"
listings_info = {"id": "68e4b036486ccc6da7273c3a", "creator_id": "68e13bd6f00164e9a246afa0", "status": "published",
                 "status_changed_at": "2025-10-06T23:16:29-07:00", "origin_domain": "us", "destination_domains": ["us"],
                 "publish_count": 1, "app_version": "6.32",
                 "inventory": {"status": "available", "status_changed_at": "2025-10-06T23:16:22-07:00",
                               "multi_item": True, "size_quantity_revision": 1, "size_quantities": [
                         {"size_id": "UNI", "quantity_available": 8, "quantity_reserved": 0, "quantity_sold": 0,
                          "size_ref": 64, "size_system": "us",
                          "size_obj": {"id": "UNI", "display": "UNI", "display_with_size_set": "UNI",
                                       "display_with_size_system": "UNI", "display_with_system_and_set": "UNI",
                                       "size_system": "us"}, "size_set_tags": []}]},
                 "catalog": {"category_features": ["011e9287d97b4e80ef00a955"], "category": "002a8975d97b4e80ef00a955",
                             "department": "000e8975d97b4e80ef00a955",
                             "department_obj": {"id": "000e8975d97b4e80ef00a955", "display": "Women", "slug": "Women",
                                                "message_id": "women"},
                             "category_obj": {"id": "002a8975d97b4e80ef00a955", "display": "Accessories",
                                              "slug": "Accessories", "message_id": "women_accessories"},
                             "category_feature_objs": [
                                 {"id": "011e9287d97b4e80ef00a955", "display": "Belts", "slug": "Belts",
                                  "message_id": "women_accessories_belts"}]}, "catalog_source": "u",
                 "inventory_unit_id": "68e4b036486ccc6da7273c3b", "updated_at": "2025-10-07T23:00:01-07:00",
                 "brand_id": "5ce421702fed0250826ff08e", "brand": "Ganni",
                 "colors": [{"name": "Cream", "rgb": "#f4e0ca", "message_id": "cream"}], "condition": "nwt",
                 "category": "Accessories",
                 "cover_shot": {"id": "68e4b03c486ccc0225273c9f", "creator_id": "68e13bd6f00164e9a246afa0",
                                "picture": "68e4b03c486ccc0225273c9f.jpg",
                                "path": "posts/2025/10/06/68e4b036486ccc6da7273c3a/m_68e4b03c486ccc0225273c9f.jpg",
                                "path_small": "posts/2025/10/06/68e4b036486ccc6da7273c3a/s_68e4b03c486ccc0225273c9f.jpg",
                                "path_large": "posts/2025/10/06/68e4b036486ccc6da7273c3a/l_68e4b03c486ccc0225273c9f.jpg",
                                "path_webp": "posts/2025/10/06/68e4b036486ccc6da7273c3a/m_wp_68e4b03c486ccc0225273c9f.webp",
                                "path_small_webp": "posts/2025/10/06/68e4b036486ccc6da7273c3a/s_wp_68e4b03c486ccc0225273c9f.webp",
                                "path_large_webp": "posts/2025/10/06/68e4b036486ccc6da7273c3a/l_wp_68e4b03c486ccc0225273c9f.webp",
                                "content_type": "image/jpeg", "storage_location": "va",
                                "md5_hash": "32ed4bdfd6f4de2e0feb5c41182e23ea",
                                "created_at": "2025-10-06T23:16:28-07:00",
                                "url": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/m_68e4b03c486ccc0225273c9f.jpg",
                                "url_small": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/s_68e4b03c486ccc0225273c9f.jpg",
                                "url_large": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/l_68e4b03c486ccc0225273c9f.jpg",
                                "url_webp": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/m_wp_68e4b03c486ccc0225273c9f.webp",
                                "url_small_webp": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/s_wp_68e4b03c486ccc0225273c9f.webp",
                                "url_large_webp": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/l_wp_68e4b03c486ccc0225273c9f.webp",
                                "content_type_alternate": "image/webp"},
                 "description": "Ganni’s Leopard beanie Hat combines bold spirit and functionality in a distinctive accessory. Crafted with a ribbed design for comfort and fit, it is embellished with an applique logo patch on the front for an iconic, contemporary touch. Perfect for adding character to winter looks.\nSeason: AW25\nComposition: GENERAL 100% Wool\nMADE IN MOLDOVA \n\n We are a small business headquartered in beautiful Minneapolis, MN, founded by leadership with over two decades of experience in the luxury goods business.\n\n All of our items are 100% Authentic, Guaranteed.\n\n We Ship Out Orders Fast - Typically within 1 business day or less.\n\n PLEASE NOTE: The pictures in our listing are of the actual product and are NOT stock photos. All of our photos are professionally taken in our warehouse studio.\n\n If you have any questions or if we can be of assistance in any way, please reach out!",
                 "original_price_amount": {"val": "221.0", "currency_code": "USD", "currency_symbol": "$"},
                 "pictures": [{"id": "68e4b03c995803df67b3bb25", "creator_id": "68e13bd6f00164e9a246afa0",
                               "picture": "68e4b03c995803df67b3bb25.jpg",
                               "path": "posts/2025/10/06/68e4b036486ccc6da7273c3a/m_68e4b03c995803df67b3bb25.jpg",
                               "path_small": "posts/2025/10/06/68e4b036486ccc6da7273c3a/s_68e4b03c995803df67b3bb25.jpg",
                               "path_large": "posts/2025/10/06/68e4b036486ccc6da7273c3a/l_68e4b03c995803df67b3bb25.jpg",
                               "path_webp": "posts/2025/10/06/68e4b036486ccc6da7273c3a/m_wp_68e4b03c995803df67b3bb25.webp",
                               "path_small_webp": "posts/2025/10/06/68e4b036486ccc6da7273c3a/s_wp_68e4b03c995803df67b3bb25.webp",
                               "path_large_webp": "posts/2025/10/06/68e4b036486ccc6da7273c3a/l_wp_68e4b03c995803df67b3bb25.webp",
                               "content_type": "image/jpeg", "storage_location": "va",
                               "md5_hash": "fe733a93145b573d89a0a30ffc7eed45",
                               "created_at": "2025-10-06T23:16:28-07:00",
                               "url": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/m_68e4b03c995803df67b3bb25.jpg",
                               "url_small": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/s_68e4b03c995803df67b3bb25.jpg",
                               "url_large": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/l_68e4b03c995803df67b3bb25.jpg",
                               "url_webp": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/m_wp_68e4b03c995803df67b3bb25.webp",
                               "url_small_webp": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/s_wp_68e4b03c995803df67b3bb25.webp",
                               "url_large_webp": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/l_wp_68e4b03c995803df67b3bb25.webp",
                               "content_type_alternate": "image/webp"},
                              {"id": "68e4b03b486ccc6931273c8a", "creator_id": "68e13bd6f00164e9a246afa0",
                               "picture": "68e4b03b486ccc6931273c8a.jpg",
                               "path": "posts/2025/10/06/68e4b036486ccc6da7273c3a/m_68e4b03b486ccc6931273c8a.jpg",
                               "path_small": "posts/2025/10/06/68e4b036486ccc6da7273c3a/s_68e4b03b486ccc6931273c8a.jpg",
                               "path_large": "posts/2025/10/06/68e4b036486ccc6da7273c3a/l_68e4b03b486ccc6931273c8a.jpg",
                               "path_webp": "posts/2025/10/06/68e4b036486ccc6da7273c3a/m_wp_68e4b03b486ccc6931273c8a.webp",
                               "path_small_webp": "posts/2025/10/06/68e4b036486ccc6da7273c3a/s_wp_68e4b03b486ccc6931273c8a.webp",
                               "path_large_webp": "posts/2025/10/06/68e4b036486ccc6da7273c3a/l_wp_68e4b03b486ccc6931273c8a.webp",
                               "content_type": "image/jpeg", "storage_location": "va",
                               "md5_hash": "cafcd9bd2e82cdaa9212a996ef2cc3ef",
                               "created_at": "2025-10-06T23:16:27-07:00",
                               "url": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/m_68e4b03b486ccc6931273c8a.jpg",
                               "url_small": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/s_68e4b03b486ccc6931273c8a.jpg",
                               "url_large": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/l_68e4b03b486ccc6931273c8a.jpg",
                               "url_webp": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/m_wp_68e4b03b486ccc6931273c8a.webp",
                               "url_small_webp": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/s_wp_68e4b03b486ccc6931273c8a.webp",
                               "url_large_webp": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/l_wp_68e4b03b486ccc6931273c8a.webp",
                               "content_type_alternate": "image/webp"}],
                 "price_amount": {"val": "333.0", "currency_code": "USD", "currency_symbol": "$"}, "size": "UNI",
                 "seller_shipping_discount_id": "60114d1aaabb081028b99217", "type": "multi_item",
                 "title": "Ganni Leopard beanie Women's Hat", "assigned_just_in_at": "2025-10-06T23:16:28-07:00",
                 "brand_update_count": 0, "first_published_at": "2025-10-06T23:16:28-07:00",
                 "first_available_at": "2025-10-06T23:16:29-07:00", "created_at": "2025-10-06T23:16:22-07:00",
                 "price": 333.0, "original_price": 221.0, "share_count": 0, "like_count": 0, "comment_count": 0,
                 "active_buyer_offer_count": 0, "post_like_page": 0, "post_comment_page": 0, "post_event_page": 0,
                 "post_event_host_shares_page": 0, "has_offer": False, "has_seller_offer": False, "videos": [],
                 "generated_story_ids": [], "style_tags": [],
                 "picture_url": "https://dvyy6pjhapp0q.cloudfront.net/posts/2025/10/06/68e4b036486ccc6da7273c3a/m_68e4b03c486ccc0225273c9f.jpg",
                 "aggregates": {"shares": 0, "comments": 0, "likes": 0, "active_buyer_offers": 0, "active_offers": 0},
                 "comments": [], "events": [], "event_host_shares": [], "likes": [], "caller_has_offered": False,
                 "offer_data": {}, "posh_pass_eligible": False, "creator_username": "cry_click529",
                 "creator_display_handle": "cry_click529", "creator_full_name": "Posh Automaton",
                 "creator_picture_url": "https://dvyy6pjhapp0q.cloudfront.net/users/2025/10/04/8/t_68e13bd8f00164e9a246afa5.jpeg",
                 "caller_has_liked": False,
                 "department": {"id": "000e8975d97b4e80ef00a955", "display": "Women", "slug": "Women",
                                "message_id": "women"},
                 "category_v2": {"id": "002a8975d97b4e80ef00a955", "display": "Accessories", "slug": "Accessories",
                                 "message_id": "women_accessories"}, "category_features": [
        {"id": "011e9287d97b4e80ef00a955", "display": "Belts", "slug": "Belts",
         "message_id": "women_accessories_belts"}],
                 "size_obj": {"id": "UNI", "display": "UNI", "display_with_size_set": "UNI",
                              "display_with_size_system": "UNI", "display_with_system_and_set": "UNI",
                              "size_system": "us"},
                 "brand_obj": {"id": "5ce421702fed0250826ff08e", "canonical_name": "Ganni", "slug": "Ganni"},
                 "shipping_discount_type": None, "deal_info": {}, "system_messages": [
        {"message": "$6.49 shipping on all orders. Bundle multiple items to save even more. <u>Details &raquo;</u>",
         "destination_url": "https://qa.goshd.com/mapp/poshmark_shipping?origin_domain=us&is_authentication_free=False",
         "image_url": "https://d134s5eieoovdn.cloudfront.net/assets/native_app/icons/icon-shipping-discount@2x.png"}, {
            "message": "Every purchase on Poshmark is protected. Get the item you ordered or get your money back. Otherwise, all sales are final. <u>Details &raquo;</u>",
            "destination_url": "https://qa.goshd.com/mapp/posh_protect",
            "image_url": "https://d134s5eieoovdn.cloudfront.net/assets/native_app/icons/poshprotect-grey-outline@2x.png"}],
                 "enhanced_system_messages": {"shipping": [{
                                                               "message": "$6.49 shipping on all orders. Bundle multiple items to save even more. <u>Details &raquo;</u>",
                                                               "destination_url": "https://qa.goshd.com/mapp/poshmark_shipping?origin_domain=us&is_authentication_free=False",
                                                               "image_url": "https://d134s5eieoovdn.cloudfront.net/assets/native_app/icons/icon-shipping-discount@2x.png",
                                                               "target_obj": {"route": "//poshmark_shipping",
                                                                              "mapp_enabled": True, "data": {},
                                                                              "params": {"origin_domain": "us",
                                                                                         "is_authentication_free": "False"}}}],
                                              "seller_discount": [], "listing_promotions": []}}
payload = {
    "user_id": str(ObjectId()),
    "listings_info": listings_info
}
thread = requests.post(url + "/api/thread/new", json=payload)
thread_id = thread.json()["id"]

while True:
    query = input("ASK AI: ")
    if query == "":
        break
    response = requests.post(url + "/api/query/" + thread_id, json={"message": query})
    print("AI Response :", response.json())
