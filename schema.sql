CREATE TABLE "auth_group" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(80) NOT NULL UNIQUE
);
CREATE TABLE "auth_group_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "group_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("group_id", "permission_id")
);
CREATE TABLE "auth_permission" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "content_type_id" integer NOT NULL,
    "codename" varchar(100) NOT NULL,
    UNIQUE ("content_type_id", "codename")
);
CREATE TABLE "auth_user" (
    "id" integer NOT NULL PRIMARY KEY,
    "password" varchar(128) NOT NULL,
    "last_login" datetime NOT NULL,
    "is_superuser" bool NOT NULL,
    "username" varchar(30) NOT NULL UNIQUE,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "email" varchar(75) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "date_joined" datetime NOT NULL
);
CREATE TABLE "auth_user_groups" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id"),
    UNIQUE ("user_id", "group_id")
);
CREATE TABLE "auth_user_user_permissions" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"),
    UNIQUE ("user_id", "permission_id")
);
CREATE TABLE "blog_post" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(255) NOT NULL,
    "slug" varchar(255) NOT NULL UNIQUE,
    "description" varchar(255) NOT NULL,
    "content" text NOT NULL,
    "published" bool NOT NULL,
    "created" datetime NOT NULL
);
CREATE TABLE "companion_catagories" (
    "id" integer NOT NULL PRIMARY KEY,
    "catagory" varchar(128) NOT NULL,
    "categoryId" varchar(128) NOT NULL
);
CREATE TABLE "companion_fabrics" (
    "id" integer NOT NULL PRIMARY KEY,
    "fabTopic_id" integer NOT NULL REFERENCES "companion_topics" ("id"),
    "fabName" varchar(128) NOT NULL,
    "fabContent" varchar(128) NOT NULL,
    "fabWeave" varchar(128) NOT NULL,
    "fabDye" varchar(128) NOT NULL,
    "fabFinish" varchar(128) NOT NULL,
    "fabDescription" varchar(8192) NOT NULL,
    "fabImage" varchar(100) NOT NULL,
    "fabImage_secondary" varchar(100) NOT NULL,
    "fabVideo" varchar(200) NOT NULL,
    "fabVideoURL" varchar(200) NOT NULL,
    "isPremium" bool NOT NULL
);
CREATE TABLE "companion_topics" (
    "id" integer NOT NULL PRIMARY KEY,
    "fabCatagory_id" integer NOT NULL REFERENCES "companion_catagories" ("id"),
    "topic" varchar(128) NOT NULL,
    "topicId" varchar(128) NOT NULL
);
CREATE TABLE "django_admin_log" (
    "id" integer NOT NULL PRIMARY KEY,
    "action_time" datetime NOT NULL,
    "user_id" integer NOT NULL,
    "content_type_id" integer,
    "object_id" text,
    "object_repr" varchar(200) NOT NULL,
    "action_flag" smallint unsigned NOT NULL,
    "change_message" text NOT NULL
);
CREATE TABLE "django_content_type" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL,
    UNIQUE ("app_label", "model")
);
CREATE TABLE "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" datetime NOT NULL
);
CREATE TABLE "login_key" (
    "id" integer NOT NULL PRIMARY KEY,
    "key" varchar(38) NOT NULL,
    "active" bool NOT NULL,
    "owner_id" integer REFERENCES "login_userprofile" ("id"),
    "keyExpiryDate" date NOT NULL
);
CREATE TABLE "login_userprofile" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id"),
    "confirmation_code" varchar(128) NOT NULL,
    "reset_code" varchar(128) NOT NULL,
    "address_lineOne" varchar(128) NOT NULL,
    "address_lineTwo" varchar(128) NOT NULL,
    "city" varchar(128) NOT NULL,
    "State" varchar(128) NOT NULL,
    "zipCode" varchar(10) NOT NULL,
    "appExpiryDate" date
);
CREATE TABLE "webstore_order" (
    "id" integer NOT NULL PRIMARY KEY,
    "purchaser_id" integer REFERENCES "login_userprofile" ("id"),
    "orderDate" datetime NOT NULL,
    "shippingCost" decimal NOT NULL,
    "totalCost" decimal NOT NULL
);
CREATE TABLE "webstore_orderitemcorrect" (
    "id" integer NOT NULL PRIMARY KEY,
    "itemCost" decimal NOT NULL,
    "itemQuantity" integer NOT NULL,
    "order_id" integer REFERENCES "webstore_order" ("id"),
    "itemID_id" integer REFERENCES "webstore_storeitem" ("id")
);
CREATE TABLE "webstore_storecategory" (
    "id" integer NOT NULL PRIMARY KEY,
    "categoryName" varchar(128) NOT NULL
);
CREATE TABLE "webstore_storeitem" (
    "id" integer NOT NULL PRIMARY KEY,
    "category_id" integer NOT NULL REFERENCES "webstore_storecategory" ("id"),
    "itemName" varchar(128) NOT NULL,
    "itemNameid" varchar(128) NOT NULL,
    "description" varchar(2048) NOT NULL,
    "price" decimal NOT NULL,
    "quantity" integer NOT NULL,
    "picture" varchar(100) NOT NULL,
    "featured_picture" varchar(100) NOT NULL,
    "isFeatured" bool NOT NULL,
    "canCalcShipping" bool NOT NULL,
    "weightPerItem" real NOT NULL,
    "numberPerBox" integer NOT NULL,
    "boxWidth" integer NOT NULL,
    "boxDepth" integer NOT NULL,
    "boxHeight" integer NOT NULL,
    "isFabric" bool NOT NULL,
    "isSmallItem" bool NOT NULL,
    "isSwatchKit" bool NOT NULL,
    "isFeltingKit" bool NOT NULL
);
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '1','Can add log entry','1','add_logentry' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '2','Can change log entry','1','change_logentry' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '3','Can delete log entry','1','delete_logentry' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '4','Can add permission','2','add_permission' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '5','Can change permission','2','change_permission' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '6','Can delete permission','2','delete_permission' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '7','Can add group','3','add_group' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '8','Can change group','3','change_group' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '9','Can delete group','3','delete_group' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '10','Can add user','4','add_user' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '11','Can change user','4','change_user' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '12','Can delete user','4','delete_user' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '13','Can add content type','5','add_contenttype' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '14','Can change content type','5','change_contenttype' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '15','Can delete content type','5','delete_contenttype' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '16','Can add session','6','add_session' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '17','Can change session','6','change_session' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '18','Can delete session','6','delete_session' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '19','Can add order table','7','add_ordertable' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '20','Can change order table','7','change_ordertable' );
INSERT INTO "auth_permission" ( "id","name","content_type_id","codename" ) VALUES ( '21','Can delete order table','7','delete_ordertable' );
INSERT INTO "auth_user" ( "id","password","last_login","is_superuser","username","first_name","last_name","email","is_staff","is_active","date_joined" ) VALUES ( '1','pbkdf2_sha256$12000$IGweLRpxbSib$xvUVB+tNX/0BH+z6FWnnQdML9dIO007gt/t7tO8xMWs=','2014-04-30 17:34:08.798685','1','admin','','','admin@email.com','1','1','2014-04-16 21:16:38.067000' );
INSERT INTO "auth_user" ( "id","password","last_login","is_superuser","username","first_name","last_name","email","is_staff","is_active","date_joined" ) VALUES ( '4','pbkdf2_sha256$12000$PHEkeY26mChJ$hHFitFFVPK0e0MnGYCAe0rG3Hqvige3EiU/OH0c+3TU=','2014-04-18 05:30:54.419000','0','george','George','Darling','ghd2d@mtmail.mtsu.edu','0','1','2014-04-18 05:29:59.157000' );
INSERT INTO "auth_user" ( "id","password","last_login","is_superuser","username","first_name","last_name","email","is_staff","is_active","date_joined" ) VALUES ( '3','pbkdf2_sha256$12000$jRcxFOaa4WI3$X9chGbdN/zzlZaX8jkPb2CVnkJBFUYOMht/nqnNGRoA=','2014-05-15 20:49:26.424983','0','pdf2e','Paul','Fuller','pdf2e@mtmail.mtsu.edu','0','1','2014-04-16 22:10:52.648000' );
INSERT INTO "auth_user" ( "id","password","last_login","is_superuser","username","first_name","last_name","email","is_staff","is_active","date_joined" ) VALUES ( '5','pbkdf2_sha256$12000$m9ISMoaxgsNi$heogfYnQXOMB9LQtTTzQNS4k+cxCQUrnwHweJQAhbyA=','2014-11-08 21:47:25.458152','1','reid','','','reid.wiggins@mtsu.edu','1','1','2014-11-08 21:47:18.944942' );
INSERT INTO "auth_user" ( "id","password","last_login","is_superuser","username","first_name","last_name","email","is_staff","is_active","date_joined" ) VALUES ( '2','pbkdf2_sha256$12000$vaAuSIE2jyFx$BqIHcTbRLEo51ZF4nMCcLT25u76Qm0KGlk2K/yq0tLw=','2014-04-16 21:49:58.470000','0','thisIsAtest','Paul','Fuller','email@gmail.com','0','0','2014-04-16 21:49:58.470000' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '1','Fibers','Fibers' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '2','Yarns','0' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '3','Basic Weaves','BasicWeaves' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '4','Fancy & Figure Weaves','FancyFigureWeaves' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '5','Narrow Weaves','NarrowWeaves' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '6','Knits','Knits' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '7','Narrow Knits','NarrowKnits' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '8','Films & Fiberweb Structures','FilmsFiberwebStructures' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '9','Composite & Multiplex Fabrics','CompositeMultiplexFabrics' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '10','Finishes','Finishes' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '11','Dyeing & Printing','DyeingPrinting' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '12','Dyeing & Printing Processes','DyeingPrintingProcesses' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '13','Dyeing & Printing & Finishing Problems','DyeingPrintingFinishingProblems' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '14','Manufacturing Equipment','ManufacturingEquipment' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '15','Handmade Lace Production','HandmadeLaceProduction' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '16','Fabric Seconds & Textile Usage Problems','FabricSecondsTextileUsageProblems' );
INSERT INTO "companion_catagories" ( "id","catagory","categoryId" ) VALUES ( '17','Review Questions','ReviewQuestions' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '1','1','Cotton','','','','','Cotton is a cellulosic fiber obtained from the seed of a cotton plant Depending on the fiber length and/or finish, fabrics can have a matte or lustrous appearance Photomicrographs courtesy of Agricultural Research Service, US Dept. of Agriculture','/media/companion/fabrics/primary/cotton1_1.jpg','/media/companion/fabrics/secondary/cotton2_1.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '2','1','Cotton Fiber','','','','','Cotton fiber after being harvested and cleaned','/media/companion/fabrics/primary/cottonfiber1_2.jpg','/media/companion/fabrics/secondary/cottonfiber2_2.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '3','1','Cotton Plant Flower','','','','','A flowering cotton plant Photographs courtesy of National Cotton Council of America','/media/companion/fabrics/primary/cottonplantflower1_2.jpg','/media/companion/fabrics/secondary/cottonplantflower2_2.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '4','1','White Cotton Boll','','','','','An open white boll of cotton','/media/companion/fabrics/primary/whitecottonboll1_2.jpg','/media/companion/fabrics/secondary/whitecottonboll2_2.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '5','1','Open Cotton Boll','','','','','These pictures show an open cotton boll Photographs courtesy of National Cotton Council of America','/media/companion/fabrics/primary/opencottonboll1_2.jpg','/media/companion/fabrics/secondary/opencottonboll2_2.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '6','1','Cotton Harvesting','','','','','Cotton being harvested  Photographs courtesy of National Cotton Council of America','/media/companion/fabrics/primary/cottonharvesting1_2.jpg','/media/companion/fabrics/secondary/cottonharvesting2_2.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '7','1','Cotton Fabric','','','','','This is a 100% cotton muslin fabric','/media/companion/fabrics/primary/cottonfabric1_2.jpg','/media/companion/fabrics/secondary/cottonfabric2_2.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '8','1','Recycled Cotton Denim','','','','','The products in this picture were made from recycled cotton','/media/companion/fabrics/primary/recycledcottondenim1_2.jpg','/media/companion/fabrics/secondary/recycledcottondenim2_2.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '9','1','Colored Cotton Boll','','','','','An open boll of naturally colored cotton','/media/companion/fabrics/primary/coloredcottonboll1_1.jpg','/media/companion/fabrics/secondary/coloredcottonboll2_1.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '10','1','Fox Fibre® Cotton','','','','','Grown in red, rust, brown, beige and green colors Twice as expensive as white cotton Colors become deeper with washing and age','/media/companion/fabrics/primary/foxfiber1.jpg','/media/companion/fabrics/secondary/foxfiber2.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '11','1','Fox Fibre® Sweater','','','','','A sweater made from naturally colored cotton Twice as expensive as white cotton Colors become deeper with washing and age','/media/companion/fabrics/primary/coloredcottonsweater1_1.jpg','/media/companion/fabrics/secondary/coloredcottonsweater2_1.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '12','1','Fox Fibre® Waffle Cloth','','','','','This fabric was woven with naturally colored cotton yarns','/media/companion/fabrics/primary/foxwaffle1_1.jpg','/media/companion/fabrics/secondary/foxwaffle2_1.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '13','1','Flax','','','','','Fiber is taken from the stem and root of the flax plant Fabrics made from flax are referred to as linen fabrics Strong, stiff fiber Poor resiliency Photomicrographs courtesy of British Textiles Technology Group','/media/companion/fabrics/primary/flax1_1.jpg','/media/companion/fabrics/secondary/flax2_1.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '14','1','Flax Fiber','','','','','Flax is a cellulosic fiber taken from the stem and root of the flax plant Fabrics made from flax are referred to as linen fabrics Strong, stiff fiber Poor resiliency','/media/companion/fabrics/primary/flaxfiber1_1.jpg','/media/companion/fabrics/secondary/flaxfiber2_1.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '15','1','Flax Stages','','','','','Retting - loosening the fibers for easy removal from the stalk Scutching - removing the woody portion of the stalks by passing them between metal fluted rollers Hackling - combing the fibers to remove the irregular and short fibers','/media/companion/fabrics/primary/flaxstages1_1.jpg','/media/companion/fabrics/secondary/flaxstages2_1.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '16','1','Flax Twine','','','','','Twine yarn made from flax','/media/companion/fabrics/primary/flaxtwine1_1.jpg','/media/companion/fabrics/secondary/flaxtwine2_1.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '17','1','Linen Carpeting','','','','','Carpet made from flax','/media/companion/fabrics/primary/linencarpeting1_1.jpg','/media/companion/fabrics/secondary/linencarpeting2_1.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '18','1','Linen Suiting','','','','','Linen fabrics are good for warm weather garments due to high heat conduction of the flax fibers','/media/companion/fabrics/primary/linensuiting1_1.jpg','/media/companion/fabrics/secondary/linensuiting2_1.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '19','1','Ramie','','','','','Cellulosic fiber also known as grasscloth or China grass Long fibers create a high luster Strongest natural fiber Used in apparel and home furnishing fabrics Photomicrographs courtesy of British Textiles Technology Group','/media/companion/fabrics/primary/ramie1_1.jpg','/media/companion/fabrics/secondary/ramie2_1.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '20','1','Ramie Fiber','','','','','Ramie fiber after being harvested and cleaned','/media/companion/fabrics/primary/ramiefiber1_1.jpg','/media/companion/fabrics/secondary/ramiefiber2_1.jpg','','','0' );
INSERT INTO "companion_fabrics" ( "id","fabTopic_id","fabName","fabContent","fabWeave","fabDye","fabFinish","fabDescription","fabImage","fabImage_secondary","fabVideo","fabVideoURL","isPremium" ) VALUES ( '21','1','Ramie Fabric','','','','','Cellulosic fiber also known as grasscloth or China grass Long fibers create a high luster Strongest natural fiber High absorbency  Moderate thermal retention','/media/companion/fabrics/primary/crashramiefabric1_1.jpg','/media/companion/fabrics/secondary/crashramiefabric2_1.jpg','','','0' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '1','1','Natural Cellulosic Fibers','NaturalCellulosicFibers' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '2','1','Natural Protein Fibers','NaturalProteinFibers' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '3','1','Synthetic Fibers','SyntheticFibers' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '4','1','Manufactured Fibers','ManufacturedFibers' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '5','1','Special Use Fibers','SpecialUseFibers' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '6','2','Spun Yarns','SpunYarns' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '7','2','Filament Yarns','FilamentYarns' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '8','2','Ply Yarns','PlyYarns' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '9','2','Novelty Yarns','NoveltyYarns' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '10','2','Yarn Twist','YarnTwist' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '11','3','Balanced Plain Weaves','BalancedPlainWeaves' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '12','3','Unbalanced Plain Weaves','UnbalancedPlainWeaves' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '13','3','Basket Weaves','BasketWeaves' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '14','3','Even-Sided Twill Weaves','Even-SidedTwillWeaves' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '15','3','Warp-Faced Twill Weaves','Warp-FacedTwillWeaves' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '16','3','Filling-Faced Twill Weaves','0' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '17','3','Warp-Faced Satin Weaves','0' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '18','3','Filling-Faced Satin Weaves','Filling-FacedSatinWeaves' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '19','4','Dobby Weaves','0' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '20','4','Extra-Yarn Weaves','0' );
INSERT INTO "companion_topics" ( "id","fabCatagory_id","topic","topicId" ) VALUES ( '21','4','Piqué Weaves','0' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '1','log entry','admin','logentry' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '3','group','auth','group' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '2','permission','auth','permission' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '4','user','auth','user' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '12','post','blog','post' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '9','catagories','companion','catagories' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '11','fabrics','companion','fabrics' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '10','topics','companion','topics' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '5','content type','contenttypes','contenttype' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '8','key','login','key' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '7','user profile','login','userprofile' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '6','session','sessions','session' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '15','order','webstore','order' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '16','order item correct','webstore','orderitemcorrect' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '13','store category','webstore','storecategory' );
INSERT INTO "django_content_type" ( "id","name","app_label","model" ) VALUES ( '14','store item','webstore','storeitem' );
INSERT INTO "django_session" ( "session_key","session_data","expire_date" ) VALUES ( 'e7y2onppmajt4mxmvsn4vvpzm4ufpxnv','NzI2NjJjYWMzNmNkZDZkYmU4MzNjZWZmZGI2MGU2ZTI4ODczMTYwNTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MywiY2FydExpc3QiOltbIkNvcnJpZWRhbGVXb29sRmliZXIiLCIxIl0sWyJTb3liZWFuRmliZXIiLCIxIl1dfQ==','2014-05-29 21:08:44.799386' );
INSERT INTO "django_session" ( "session_key","session_data","expire_date" ) VALUES ( '9b6l88zbxppuv4a07erae7nvuz7r9kia','NDk3MTk5ODg2NGZkNWMxNDM4NmFiOTgwMTM3MzExN2ZiNTA3NzM2ZDp7ImNhcnRMaXN0IjpbXSwiX2F1dGhfdXNlcl9pZCI6NSwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==','2014-11-22 21:51:51.676522' );
INSERT INTO "login_userprofile" ( "id","user_id","confirmation_code","reset_code","address_lineOne","address_lineTwo","city","State","zipCode","appExpiryDate" ) VALUES ( '1','2','TMiaORDCJa4pY15SVZZoFczkEdvbl8Cao','','','','','','',NULL );
INSERT INTO "login_userprofile" ( "id","user_id","confirmation_code","reset_code","address_lineOne","address_lineTwo","city","State","zipCode","appExpiryDate" ) VALUES ( '2','3','kVcDpNGZytPJ9vW8FYaYW6Bju79Bf0v8l','','','','','','',NULL );
INSERT INTO "login_userprofile" ( "id","user_id","confirmation_code","reset_code","address_lineOne","address_lineTwo","city","State","zipCode","appExpiryDate" ) VALUES ( '3','4','vAIy8tzRIiCSEYW01bxd4Kye6dryMYBt6','','','','','','',NULL );
INSERT INTO "webstore_order" ( "id","purchaser_id","orderDate","shippingCost","totalCost" ) VALUES ( '1',NULL,'2014-04-28 18:04:31.104000','1','2' );
INSERT INTO "webstore_order" ( "id","purchaser_id","orderDate","shippingCost","totalCost" ) VALUES ( '2',NULL,'2014-04-29 22:45:07.791000','1','10.95' );
INSERT INTO "webstore_order" ( "id","purchaser_id","orderDate","shippingCost","totalCost" ) VALUES ( '3',NULL,'2014-04-30 13:44:20.954000','1','10.95' );
INSERT INTO "webstore_order" ( "id","purchaser_id","orderDate","shippingCost","totalCost" ) VALUES ( '4',NULL,'2014-04-30 13:45:27.872000','1','10.95' );
INSERT INTO "webstore_order" ( "id","purchaser_id","orderDate","shippingCost","totalCost" ) VALUES ( '5',NULL,'2014-04-30 17:19:12.883208','0','9.95' );
INSERT INTO "webstore_order" ( "id","purchaser_id","orderDate","shippingCost","totalCost" ) VALUES ( '6',NULL,'2014-04-30 17:20:22.406115','0','9.95' );
INSERT INTO "webstore_order" ( "id","purchaser_id","orderDate","shippingCost","totalCost" ) VALUES ( '7',NULL,'2014-05-15 21:09:08.675552','0','9.5' );
INSERT INTO "webstore_orderitemcorrect" ( "id","itemCost","itemQuantity","order_id","itemID_id" ) VALUES ( '1','9.95','1','1','4' );
INSERT INTO "webstore_orderitemcorrect" ( "id","itemCost","itemQuantity","order_id","itemID_id" ) VALUES ( '3','9.95','1','2','4' );
INSERT INTO "webstore_orderitemcorrect" ( "id","itemCost","itemQuantity","order_id","itemID_id" ) VALUES ( '4','9.95','1','3','4' );
INSERT INTO "webstore_orderitemcorrect" ( "id","itemCost","itemQuantity","order_id","itemID_id" ) VALUES ( '5','9.95','1','4','4' );
INSERT INTO "webstore_orderitemcorrect" ( "id","itemCost","itemQuantity","order_id","itemID_id" ) VALUES ( '6','9.95','1','5','4' );
INSERT INTO "webstore_orderitemcorrect" ( "id","itemCost","itemQuantity","order_id","itemID_id" ) VALUES ( '7','9.95','1','6','4' );
INSERT INTO "webstore_orderitemcorrect" ( "id","itemCost","itemQuantity","order_id","itemID_id" ) VALUES ( '2','12.95','1','1','5' );
INSERT INTO "webstore_orderitemcorrect" ( "id","itemCost","itemQuantity","order_id","itemID_id" ) VALUES ( '8','3.5','1','7','6' );
INSERT INTO "webstore_orderitemcorrect" ( "id","itemCost","itemQuantity","order_id","itemID_id" ) VALUES ( '9','6','1','7','11' );
INSERT INTO "webstore_storecategory" ( "id","categoryName" ) VALUES ( '1','Fiber Arts' );
INSERT INTO "webstore_storecategory" ( "id","categoryName" ) VALUES ( '2','Forensic Testing Supplies' );
INSERT INTO "webstore_storecategory" ( "id","categoryName" ) VALUES ( '3','High School Teaching Materials' );
INSERT INTO "webstore_storecategory" ( "id","categoryName" ) VALUES ( '4','Swatch Kit Add-Ons' );
INSERT INTO "webstore_storecategory" ( "id","categoryName" ) VALUES ( '5','Swatch Kits' );
INSERT INTO "webstore_storecategory" ( "id","categoryName" ) VALUES ( '6','Swatch Kits for Interior Design' );
INSERT INTO "webstore_storecategory" ( "id","categoryName" ) VALUES ( '7','Testing & Analysis' );
INSERT INTO "webstore_storecategory" ( "id","categoryName" ) VALUES ( '8','Textiles Software' );
INSERT INTO "webstore_storecategory" ( "id","categoryName" ) VALUES ( '9','Videos' );
INSERT INTO "webstore_storeitem" ( "id","category_id","itemName","itemNameid","description","price","quantity","picture","featured_picture","isFeatured","canCalcShipping","weightPerItem","numberPerBox","boxWidth","boxDepth","boxHeight","isFabric","isSmallItem","isSwatchKit","isFeltingKit" ) VALUES ( '4','1','Banana Fiber ','bananafiber','Banana fiber is a natural bast fiber. It has its own physical and chemical characteristics and many other properties that make it a fine quality fiber.Small pieces of these trunks are put through a softening process for mechanical extraction of the fibers, and then bleaching, and drying. The fiber obtained thus has appearance similar to silk which has become popular as banana silk fiber yarn. ','9.95','1','/media/store/products/product_150_5.jpg','','0','0','0.0','0','0','0','0','0','0','0','0' );
INSERT INTO "webstore_storeitem" ( "id","category_id","itemName","itemNameid","description","price","quantity","picture","featured_picture","isFeatured","canCalcShipping","weightPerItem","numberPerBox","boxWidth","boxDepth","boxHeight","isFabric","isSmallItem","isSwatchKit","isFeltingKit" ) VALUES ( '5','1','Cashmere Fiber','CashmereFiber','Cashmere is characterized by its fine, soft fibers. It provides a natural light-weight insulation without bulk. Fibers are highly adaptable and easily spun into yarns and light to heavy-weight fabrics. The original undyed or natural colors of cashmere wool are various shades of grey, brown and white.','12.95','1','/media/store/products/product_153.jpg','','0','0','0.0','0','0','0','0','0','0','0','0' );
INSERT INTO "webstore_storeitem" ( "id","category_id","itemName","itemNameid","description","price","quantity","picture","featured_picture","isFeatured","canCalcShipping","weightPerItem","numberPerBox","boxWidth","boxDepth","boxHeight","isFabric","isSmallItem","isSwatchKit","isFeltingKit" ) VALUES ( '6','1','Corriedale Wool Fiber','CorriedaleWoolFiber',' Contact us for color choices or for ordering pounds! ($40/lb)','3.5','1','/media/store/products/product_157.jpg','','0','0','0.0','0','0','0','0','0','0','0','0' );
INSERT INTO "webstore_storeitem" ( "id","category_id","itemName","itemNameid","description","price","quantity","picture","featured_picture","isFeatured","canCalcShipping","weightPerItem","numberPerBox","boxWidth","boxDepth","boxHeight","isFabric","isSmallItem","isSwatchKit","isFeltingKit" ) VALUES ( '7','1','Merino Wool Fiber','MerinoWoolFiber','Contact us for color choices and for ordering pounds! ($45/lb)  Merino wool is finely crimped and soft. Staples are commonly 65 – 100 mm (2.5 - 4 inches) long.','4.25','1','/media/store/products/product_156.jpg','','0','0','0.0','0','0','0','0','0','0','0','0' );
INSERT INTO "webstore_storeitem" ( "id","category_id","itemName","itemNameid","description","price","quantity","picture","featured_picture","isFeatured","canCalcShipping","weightPerItem","numberPerBox","boxWidth","boxDepth","boxHeight","isFabric","isSmallItem","isSwatchKit","isFeltingKit" ) VALUES ( '8','1','Nettle Yarn','NettleYarn','The nettle plant is found naturally in the wild in remote mountainous areas. The fibers are processed and spun by hand. The resulting yarn has a natural and rustic appeal. Nettle yarn has a texture similar to natural linen and like linen will soften with wear. Nettle is a natural moth repellent and is often used in Nepal for backing wool carpets.','6.5','1','/media/store/products/product_155.jpg','','0','0','0.0','0','0','0','0','0','0','0','0' );
INSERT INTO "webstore_storeitem" ( "id","category_id","itemName","itemNameid","description","price","quantity","picture","featured_picture","isFeatured","canCalcShipping","weightPerItem","numberPerBox","boxWidth","boxDepth","boxHeight","isFabric","isSmallItem","isSwatchKit","isFeltingKit" ) VALUES ( '9','1','Seacell Fiber','SeacellFiber','SeaCell®pure is a cellulose fiber containing seaweed (e.g. ascophyllum nodosum). The idea behind SeaCell®pure is actually quite simple: The natural raw materials cellulose and seaweed represent the basis for the manufacture of the SeaCell®pure fiber, employing the "Lyocell Process". The cellulose fibers act as functional substrate for the seaweed','9.95','1','/media/store/products/product_152.jpg','','0','0','0.0','0','0','0','0','0','0','0','0' );
INSERT INTO "webstore_storeitem" ( "id","category_id","itemName","itemNameid","description","price","quantity","picture","featured_picture","isFeatured","canCalcShipping","weightPerItem","numberPerBox","boxWidth","boxDepth","boxHeight","isFabric","isSmallItem","isSwatchKit","isFeltingKit" ) VALUES ( '10','1','Silk Scarf','SilkScarf','14" x 59"   8mm 100% silk, hemmed edges','6.5','1','/media/store/products/product_154.jpg','','0','0','0.0','0','0','0','0','0','0','0','0' );
INSERT INTO "webstore_storeitem" ( "id","category_id","itemName","itemNameid","description","price","quantity","picture","featured_picture","isFeatured","canCalcShipping","weightPerItem","numberPerBox","boxWidth","boxDepth","boxHeight","isFabric","isSmallItem","isSwatchKit","isFeltingKit" ) VALUES ( '11','1','Soybean Fiber','SoybeanFiber','A manufactured fiber in which the fiberforming substance is composed of any regenerated, naturally occurring soybean protein.','6','1','/media/store/products/product_151.jpg','','0','0','0.0','0','0','0','0','0','0','0','0' );
INSERT INTO "webstore_storeitem" ( "id","category_id","itemName","itemNameid","description","price","quantity","picture","featured_picture","isFeatured","canCalcShipping","weightPerItem","numberPerBox","boxWidth","boxDepth","boxHeight","isFabric","isSmallItem","isSwatchKit","isFeltingKit" ) VALUES ( '12','1','The Felting Kit','TheFeltingKit','	Students can learn the basics of felting with our latest product, The Felting Kit!   The Felting Kit will encourage students’ creativity in a unique way by creating usable and wearable works of art!   Felting is a skill that can be enjoyed for many years!   10 Felting Assignments Uniquely Felt by Christine White** Easy to Follow Instructions All Needed Materials for Felting Wool Fiber Provided for Each Assignment Images of Assignments Provided to Students Images & Videos Provided to Instructors Complimentary Scarf for a Bonus Assignment Additional Images of Felted Examples   ISBN: 978-1-936480-01-2 *Complimentary instructor kit with orders of 10+     The Felting Kit includes   1.	Plastic tote 2.	Wooden dowel 3.	Bubble packaging squares (2) 4.	White chiffon fabric 5.	Waterproof apron 6.	Measuring tape 7.	Rubber bands for wooden dowel (4) 8.	Pin back and leather sample (2) 9.	Bonus silk scarf 10.	Glass beads and small rubber bands (5) 11.	Soap 12.	Wool roving (11 bags) 13.	Small plastic bowl 14.	Uniquely Felt textbook   *"Textbook is provided for supplemental reading and additional knowledge of felting. Assignments in The Felting Kit are not found in Uniquely Felt. ','89.95','1','/media/store/products/product_162.jpg','','0','0','0.0','0','0','0','0','0','0','0','0' );
INSERT INTO "webstore_storeitem" ( "id","category_id","itemName","itemNameid","description","price","quantity","picture","featured_picture","isFeatured","canCalcShipping","weightPerItem","numberPerBox","boxWidth","boxDepth","boxHeight","isFabric","isSmallItem","isSwatchKit","isFeltingKit" ) VALUES ( '13','2','Fiber Samples Packet','FiberSamplesPacket',' The Fiber Samples Packet contains 25 different fibers and a burn test chart.  Fox Fibre Cotton Flax Ramie Hemp Silk Wool Mohair Alpaca Angora Yak Camel''s Hair Rayon Acetate Lyocell Nylon Polyester Olefin Acrylic Modacrylic Spandex Aramid Glass Vinyon PLA/Ingeo™','16.95','1','/media/store/products/product_115_3.jpg','','0','0','0.0','0','0','0','0','0','0','0','0' );
INSERT INTO "webstore_storeitem" ( "id","category_id","itemName","itemNameid","description","price","quantity","picture","featured_picture","isFeatured","canCalcShipping","weightPerItem","numberPerBox","boxWidth","boxDepth","boxHeight","isFabric","isSmallItem","isSwatchKit","isFeltingKit" ) VALUES ( '14','2','Multifiber Fabric (13 Fibers)','MultifiberFabric13Fibers',' Fiber Contents Consist Of:  Spun Diacetate SEF (modacrylic) Filament Acetate Bleached Cotton Creslan 61 (acrylic) Dacron 54 (polyester) Dacron 64 (polyester)  Nylon 66 (polyamide)  Orlon 75 (acrylic)  Spun Silk Polypropylene (polyolefin) Viscose (rayon) Wool (worsted)   5" Wide Sold by the yard. Multifiber fabric used in testing and analysis of fiber contents.','6','1','/media/store/products/product_116.jpg','','0','0','0.0','0','0','0','0','0','0','0','0' );
INSERT INTO "webstore_storeitem" ( "id","category_id","itemName","itemNameid","description","price","quantity","picture","featured_picture","isFeatured","canCalcShipping","weightPerItem","numberPerBox","boxWidth","boxDepth","boxHeight","isFabric","isSmallItem","isSwatchKit","isFeltingKit" ) VALUES ( '15','2','Multifiber Fabric (6 Fibers)','MultifiberFabric6Fibers',' Multifiber Fabric used for testing and analysis of fiber contents. Fiber Contents Consist Of:  Spun Diacetate Bleached Cotton Spun Polyamide (Nylon 6.6) Spun Polyester (Dacron 54) Spun Polyacryle (Orlon 75) Worsted Wool  4" wide Sold by the yard.','6','1','/media/store/products/product_117_1.jpg','','0','0','0.0','0','0','0','0','0','0','0','0' );
INSERT INTO "webstore_storeitem" ( "id","category_id","itemName","itemNameid","description","price","quantity","picture","featured_picture","isFeatured","canCalcShipping","weightPerItem","numberPerBox","boxWidth","boxDepth","boxHeight","isFabric","isSmallItem","isSwatchKit","isFeltingKit" ) VALUES ( '16','2','Textile Id Manual & Textile Collection','TextileIdManualTextileCollection',' 123 - 2.5" Warp x 2" Filling Apparel and Interior Fabric Swatches 16 Fiber clusters representing all fiber classifications (for classroom orders fibers are sent to instructor for distribution) 21 Yarn Lengths representing various classes and constructions (for classrooms orders yarns are sent to instructor for distribution) Lab Manual complete with identification guidelines and mounting sheets organized in the the following Six Exercises: Textile Structure Identification Fiber Identification Yarn Identification Fabric Construction Identification Colored Fabric Identification Finish Identification Students are challenged to discover the identity of the items in the collection because the specific names/identities are not revealed Corresponds directly to Textile Science by Kathryn Hatch','68.95','0','/media/store/products/product_114.jpg','','0','0','0.0','0','0','0','0','0','0','0','0' );
INSERT INTO "webstore_storeitem" ( "id","category_id","itemName","itemNameid","description","price","quantity","picture","featured_picture","isFeatured","canCalcShipping","weightPerItem","numberPerBox","boxWidth","boxDepth","boxHeight","isFabric","isSmallItem","isSwatchKit","isFeltingKit" ) VALUES ( '17','3','High School Textile Swatch Kit','HighSchoolTextileSwatchKit',' The High School Textile Swatch Kit was designed exclusively for high school level fashion and interior design courses. This kit was developed from feedback of our recent survey taken by high school educators.  48 4" Warp x 3" Filling Apparel and Interior Fabric Swatches Mounting Sheets Master List (includes fabric name, description and fiber content) Three Ring Binder for Organization *Complimentary Instructor Swatch Kit with a classroom order of swatch kits.*  Instructor Swatch Kit Includes: Student Swatch Kit Manual Containing Detailed Information Including: Yarn Type Fabric Description Dye/Print Method Finish Color Guide and Yarn Count Suggested End Uses','35.95','1','/media/store/products/product_122.jpg','','0','0','0.0','0','0','0','0','0','0','0','0' );
CREATE INDEX "auth_group_permissions_5f412f9a" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_83d7f98b" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_permission_37ef4eb4" ON "auth_permission" ("content_type_id");
CREATE INDEX "auth_user_groups_5f412f9a" ON "auth_user_groups" ("group_id");
CREATE INDEX "auth_user_groups_6340c63c" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_user_permissions_6340c63c" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_83d7f98b" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "companion_fabrics_05d33704" ON "companion_fabrics" ("fabTopic_id");
CREATE INDEX "companion_topics_41fcf66b" ON "companion_topics" ("fabCatagory_id");
CREATE INDEX "django_admin_log_37ef4eb4" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_6340c63c" ON "django_admin_log" ("user_id");
CREATE INDEX "django_session_b7b81f0c" ON "django_session" ("expire_date");
CREATE INDEX "login_key_cb902d83" ON "login_key" ("owner_id");
CREATE INDEX "webstore_order_715d88f5" ON "webstore_order" ("purchaser_id");
CREATE INDEX "webstore_orderitemcorrect_68d25c7a" ON "webstore_orderitemcorrect" ("order_id");
CREATE INDEX "webstore_orderitemcorrect_b31b551f" ON "webstore_orderitemcorrect" ("itemID_id");
CREATE INDEX "webstore_storeitem_6f33f001" ON "webstore_storeitem" ("category_id");
