"""
Module containing dinner recipe data.
"""

# Collection of dinner recipes
DINNER_RECIPES = [
    {
        "name": "Spaghetti Bolognese",
        "ingredients": [
            "1 pound ground beef",
            "1 onion, diced",
            "3 cloves garlic, minced",
            "1 carrot, finely diced",
            "1 celery stalk, finely diced",
            "1 can (28 oz) crushed tomatoes",
            "2 tablespoons tomato paste",
            "1 teaspoon dried oregano",
            "1 teaspoon dried basil",
            "1/2 cup red wine (optional)",
            "1 pound spaghetti",
            "Salt and pepper to taste",
            "Grated Parmesan cheese for serving"
        ],
        "instructions": [
            "Heat a large skillet over medium heat.",
            "Add ground beef and cook until browned, breaking it up as it cooks.",
            "Add onion, garlic, carrot, and celery. Cook until vegetables are softened.",
            "Pour in red wine if using and simmer until reduced by half.",
            "Add crushed tomatoes, tomato paste, oregano, and basil.",
            "Simmer on low heat for at least 30 minutes, stirring occasionally.",
            "Meanwhile, cook spaghetti according to package instructions.",
            "Season sauce with salt and pepper to taste.",
            "Serve sauce over drained spaghetti and top with grated Parmesan cheese."
        ],
        "DifficultyLevel": "medium",
        "MealCategory": "dinner"
    },
    {
        "name": "Grilled Salmon",
        "ingredients": [
            "4 salmon fillets (6 oz each)",
            "2 tablespoons olive oil",
            "2 tablespoons lemon juice",
            "2 cloves garlic, minced",
            "1 teaspoon dried dill",
            "Salt and pepper to taste",
            "Lemon wedges for serving"
        ],
        "instructions": [
            "Preheat grill to medium-high heat.",
            "In a small bowl, mix olive oil, lemon juice, garlic, and dill.",
            "Season salmon fillets with salt and pepper.",
            "Brush the marinade over the salmon fillets.",
            "Grill salmon for 4-5 minutes per side, or until fish flakes easily with a fork.",
            "Serve with lemon wedges."
        ],
        "DifficultyLevel": "easy",
        "MealCategory": "dinner"
    },
    {
        "name": "Beef Stir Fry",
        "ingredients": [
            "1 pound flank steak, thinly sliced",
            "2 tablespoons vegetable oil",
            "1 bell pepper, sliced",
            "1 onion, sliced",
            "2 cups broccoli florets",
            "2 carrots, julienned",
            "3 cloves garlic, minced",
            "1 tablespoon ginger, minced",
            "For the sauce:",
            "1/4 cup soy sauce",
            "2 tablespoons oyster sauce",
            "1 tablespoon brown sugar",
            "1 teaspoon sesame oil",
            "1 tablespoon cornstarch",
            "1/4 cup water",
            "Cooked rice for serving"
        ],
        "instructions": [
            "In a small bowl, mix sauce ingredients and set aside.",
            "Heat 1 tablespoon oil in a large wok or skillet over high heat.",
            "Add beef and stir-fry for 2-3 minutes until browned. Remove and set aside.",
            "Add remaining oil to the wok.",
            "Add garlic and ginger, stir-fry for 30 seconds until fragrant.",
            "Add vegetables and stir-fry for 4-5 minutes until crisp-tender.",
            "Return beef to the wok.",
            "Pour sauce over the beef and vegetables.",
            "Stir-fry for 1-2 minutes until sauce thickens.",
            "Serve over cooked rice."
        ],
        "DifficultyLevel": "medium",
        "MealCategory": "dinner"
    },
    {
        "name": "Vegetable Lasagna",
        "ingredients": [
            "9 lasagna noodles",
            "2 tablespoons olive oil",
            "1 onion, diced",
            "3 cloves garlic, minced",
            "1 zucchini, diced",
            "1 bell pepper, diced",
            "8 oz mushrooms, sliced",
            "2 cups spinach",
            "1 jar (24 oz) marinara sauce",
            "15 oz ricotta cheese",
            "1 egg",
            "1/4 cup fresh basil, chopped",
            "2 cups shredded mozzarella cheese",
            "1/2 cup grated Parmesan cheese",
            "Salt and pepper to taste"
        ],
        "instructions": [
            "Preheat oven to 375°F (190°C).",
            "Cook lasagna noodles according to package instructions. Drain and set aside.",
            "Heat olive oil in a large skillet over medium heat.",
            "Add onion and garlic, cook until softened.",
            "Add zucchini, bell pepper, and mushrooms. Cook until vegetables are tender.",
            "Stir in spinach until wilted. Season with salt and pepper.",
            "In a bowl, mix ricotta cheese, egg, and basil.",
            "Spread 1/2 cup marinara sauce in the bottom of a 9x13 inch baking dish.",
            "Layer 3 lasagna noodles, 1/3 of the ricotta mixture, 1/3 of the vegetables, 1/3 of the remaining marinara, and 1/3 of the mozzarella.",
            "Repeat layers twice more.",
            "Sprinkle Parmesan cheese on top.",
            "Cover with foil and bake for 25 minutes.",
            "Remove foil and bake for an additional 10-15 minutes until cheese is bubbly and golden.",
            "Let stand for 10 minutes before serving."
        ],
        "DifficultyLevel": "difficult",
        "MealCategory": "dinner"
    },
    {
        "name": "Chicken Curry",
        "ingredients": [
            "2 pounds chicken thighs, cut into pieces",
            "2 tablespoons vegetable oil",
            "1 onion, diced",
            "3 cloves garlic, minced",
            "1 tablespoon ginger, minced",
            "2 tablespoons curry powder",
            "1 teaspoon ground cumin",
            "1 teaspoon ground coriander",
            "1/2 teaspoon turmeric",
            "1/4 teaspoon cayenne pepper (optional)",
            "1 can (14 oz) coconut milk",
            "1 can (14.5 oz) diced tomatoes",
            "1 cup chicken broth",
            "2 potatoes, diced",
            "1 cup frozen peas",
            "Salt to taste",
            "Fresh cilantro for garnish",
            "Cooked rice for serving"
        ],
        "instructions": [
            "Heat oil in a large pot over medium-high heat.",
            "Add chicken and cook until browned on all sides. Remove and set aside.",
            "In the same pot, add onion and cook until softened.",
            "Add garlic and ginger, cook for 1 minute until fragrant.",
            "Stir in curry powder, cumin, coriander, turmeric, and cayenne pepper. Cook for 1 minute.",
            "Add coconut milk, diced tomatoes, and chicken broth. Stir to combine.",
            "Return chicken to the pot and add potatoes.",
            "Bring to a boil, then reduce heat and simmer for 20-25 minutes until chicken is cooked through and potatoes are tender.",
            "Stir in frozen peas and cook for 5 more minutes.",
            "Season with salt to taste.",
            "Garnish with fresh cilantro and serve over rice."
        ],
        "DifficultyLevel": "medium",
        "MealCategory": "dinner"
    },
    {
        "name": "Baked Lemon Herb Cod",
        "ingredients": [
            "4 cod fillets (6 oz each)",
            "2 tablespoons olive oil",
            "2 tablespoons lemon juice",
            "2 cloves garlic, minced",
            "1 teaspoon dried thyme",
            "1 teaspoon dried oregano",
            "1/2 teaspoon paprika",
            "Salt and pepper to taste",
            "1 lemon, sliced",
            "Fresh parsley for garnish"
        ],
        "instructions": [
            "Preheat oven to 400°F (200°C).",
            "In a small bowl, mix olive oil, lemon juice, garlic, thyme, oregano, and paprika.",
            "Place cod fillets in a baking dish.",
            "Season with salt and pepper.",
            "Pour the herb mixture over the fish.",
            "Top with lemon slices.",
            "Bake for 15-18 minutes until fish flakes easily with a fork.",
            "Garnish with fresh parsley before serving."
        ],
        "DifficultyLevel": "easy",
        "MealCategory": "dinner"
    },
    {
        "name": "Mushroom Risotto",
        "ingredients": [
            "1 1/2 cups Arborio rice",
            "6 cups chicken or vegetable broth, warmed",
            "1/2 cup dry white wine",
            "8 oz mushrooms, sliced",
            "1 small onion, finely diced",
            "3 cloves garlic, minced",
            "2 tablespoons olive oil",
            "2 tablespoons butter",
            "1/2 cup grated Parmesan cheese",
            "2 tablespoons fresh parsley, chopped",
            "Salt and pepper to taste"
        ],
        "instructions": [
            "In a large skillet, heat 1 tablespoon olive oil over medium heat.",
            "Add mushrooms and cook until browned, about 5 minutes. Remove and set aside.",
            "In the same skillet, heat remaining olive oil and 1 tablespoon butter.",
            "Add onion and cook until translucent, about 3 minutes.",
            "Add garlic and cook for 1 minute until fragrant.",
            "Add rice and stir to coat with oil and butter.",
            "Pour in wine and stir until absorbed.",
            "Add warm broth 1/2 cup at a time, stirring constantly and waiting until liquid is absorbed before adding more.",
            "Continue until rice is creamy and tender, about 20-25 minutes.",
            "Stir in cooked mushrooms, remaining butter, and Parmesan cheese.",
            "Season with salt and pepper to taste.",
            "Garnish with fresh parsley before serving."
        ],
        "DifficultyLevel": "difficult",
        "MealCategory": "dinner"
    },
    {
        "name": "Beef Tacos",
        "ingredients": [
            "1 pound ground beef",
            "1 onion, diced",
            "2 cloves garlic, minced",
            "1 tablespoon chili powder",
            "1 teaspoon ground cumin",
            "1/2 teaspoon paprika",
            "1/2 teaspoon dried oregano",
            "1/4 teaspoon cayenne pepper (optional)",
            "Salt and pepper to taste",
            "8 taco shells or small tortillas",
            "Toppings: shredded lettuce, diced tomatoes, shredded cheese, sour cream, diced avocado, salsa"
        ],
        "instructions": [
            "Heat a large skillet over medium-high heat.",
            "Add ground beef and cook until browned, breaking it up as it cooks.",
            "Add onion and garlic, cook until softened.",
            "Stir in chili powder, cumin, paprika, oregano, cayenne pepper, salt, and pepper.",
            "Cook for 2-3 minutes until spices are fragrant.",
            "If using taco shells, warm them according to package instructions.",
            "Assemble tacos by filling shells or tortillas with beef mixture and desired toppings."
        ],
        "DifficultyLevel": "easy",
        "MealCategory": "dinner"
    },
    {
        "name": "Eggplant Parmesan",
        "ingredients": [
            "2 large eggplants, sliced into 1/2-inch rounds",
            "Salt for drawing out moisture",
            "2 cups Italian breadcrumbs",
            "1/2 cup grated Parmesan cheese, plus more for serving",
            "3 eggs, beaten",
            "1/4 cup milk",
            "1 cup all-purpose flour",
            "Vegetable oil for frying",
            "3 cups marinara sauce",
            "2 cups shredded mozzarella cheese",
            "1/4 cup fresh basil, chopped"
        ],
        "instructions": [
            "Sprinkle eggplant slices with salt and let sit for 30 minutes to draw out moisture. Pat dry with paper towels.",
            "Preheat oven to 375°F (190°C).",
            "Set up three shallow dishes: one with flour, one with beaten eggs and milk, and one with breadcrumbs mixed with Parmesan cheese.",
            "Dredge each eggplant slice in flour, then dip in egg mixture, then coat with breadcrumb mixture.",
            "Heat oil in a large skillet over medium heat.",
            "Fry eggplant slices until golden brown on both sides, about 2-3 minutes per side. Drain on paper towels.",
            "Spread 1/2 cup marinara sauce in the bottom of a 9x13 inch baking dish.",
            "Arrange a layer of eggplant slices over the sauce.",
            "Top with 1 cup marinara sauce and 1/2 cup mozzarella cheese.",
            "Repeat layers, ending with mozzarella cheese on top.",
            "Bake for 25-30 minutes until cheese is bubbly and golden.",
            "Sprinkle with fresh basil before serving."
        ],
        "DifficultyLevel": "difficult",
        "MealCategory": "dinner"
    },
    {
        "name": "Shrimp Scampi",
        "ingredients": [
            "1 pound large shrimp, peeled and deveined",
            "8 oz linguine pasta",
            "4 tablespoons butter",
            "4 tablespoons olive oil",
            "4 cloves garlic, minced",
            "1/2 teaspoon red pepper flakes",
            "1/2 cup dry white wine",
            "1 lemon, juiced",
            "1/4 cup fresh parsley, chopped",
            "Salt and pepper to taste",
            "Grated Parmesan cheese for serving"
        ],
        "instructions": [
            "Cook pasta according to package instructions. Drain and set aside.",
            "In a large skillet, heat 2 tablespoons butter and 2 tablespoons olive oil over medium-high heat.",
            "Add shrimp, salt, and pepper. Cook for 2-3 minutes until shrimp are pink and opaque. Remove and set aside.",
            "In the same skillet, add remaining butter and olive oil.",
            "Add garlic and red pepper flakes. Cook for 1 minute until fragrant.",
            "Pour in white wine and lemon juice. Bring to a simmer and cook for 2-3 minutes.",
            "Return shrimp to the skillet and add cooked pasta. Toss to combine.",
            "Stir in parsley and adjust seasoning if needed.",
            "Serve with grated Parmesan cheese."
        ],
        "DifficultyLevel": "medium",
        "MealCategory": "dinner"
    }
]