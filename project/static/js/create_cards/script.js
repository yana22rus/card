let class_card = document.querySelector(".class_card")


let arr1 = ["Strength", "Intelligence", "Willpower", "Agility", "Endurance", "Netural"]

let arr2 = ["Archer", "Assassin", "Battlemage", "Crusader", "Mage", "Monk", "Scout", "Sorcerer", "Spellsword", "Warrior"]


function create_optgroup(arr, label) {

    let optgroup_label = document.createElement("optgroup")
    optgroup_label.setAttribute("label", label)
    class_card.add(optgroup_label);
    for (x of arr) {
        let option = document.createElement("option");
        option.text = x;
        class_card.add(option);

    }

}

create_optgroup(arr1, "Одноцветные")
create_optgroup(arr2, "Мультиатрибут")

function disabled_menu(call = true) {

    let attack_card = document.querySelector("#attack_card")
    let life_card = document.querySelector("#life_card")
    let keyword_card = document.querySelector("#keyword_card")
    if (call) {
        attack_card.setAttribute("hidden", "")
        life_card.setAttribute("hidden", "")
        keyword_card.setAttribute("hidden", "")
    } else {
        attack_card.removeAttribute('hidden');
        life_card.removeAttribute('hidden');
        keyword_card.removeAttribute('hidden');
    }


}


function update() {
    let select = document.querySelector('#type_card');
    let option = select.options[select.selectedIndex];
    let form = document.querySelector("#form_create_card")

    if (option.text === "Support") {
        disabled_menu()
        let create_select = document.createElement("select")
        create_select.setAttribute("id", "uses_support")
        create_select.setAttribute("name", "uses_support")

        let lst = ["Бесконечно"]

        for (let i = 1; i <= 12; i++) {
            lst.push(String(i))
        }

        for (x of lst) {
            let option = document.createElement("option");
            option.text = x;
            create_select.add(option)

        }


        form.appendChild(create_select)

    } else {
        disabled_menu(false)
        let el = document.querySelector("#uses_support");
        if (typeof (el) != 'undefined' && el != null) {
            el.remove();
        }


    }

}

let image_input = document.querySelector("#img_input")
let uploaded_image = "";


image_input.addEventListener("change", function () {
    let reader = new FileReader()
    reader.addEventListener("load", () => {
        uploaded_image = reader.result
        document.querySelector("#display_image").style.backgroundImage = `url(${uploaded_image})`
    });

    reader.readAsDataURL(this.files[0])


})

update()

function save_selected_value(type_creature,keyword_card,mechanics_card) {

    selected_value(type_creature,"#type_creature")
    selected_value(keyword_card,"#keyword_card")
    selected_value(mechanics_card,"#mechanics_card")


}

function selected_value(data,locator){

    options = Array.from(document.querySelector(locator));

    data.forEach(function (v) {
        options.find(c => c.value == v).selected = true;
    });


}