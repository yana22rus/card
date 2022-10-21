function foo(data) {

    let i = data.length;

    for (let x = 0; x<i;x++) {

        let table = document.createElement("table")
        table.setAttribute("width", "33%")
        table.setAttribute("cellpadding", "5")
        table.setAttribute("border", "1")

        let mp_title = document.createElement("tr")

        let td1 = document.createElement("td")
        td1.innerText = data[x]["mana_card"];
        let td2 = document.createElement("td")
        td2.innerText = data[x]["title"];
        td2.setAttribute("colspan", "2")

        mp_title.appendChild(td1)
        mp_title.appendChild(td2)

        let life_img_attack = document.createElement("tr")

        let td3 = document.createElement("td")
        td3.setAttribute("width", "100px")
        td3.setAttribute("height", "300px")
        td3.innerText =  data[x]["attack_card"];
        let td4 = document.createElement("td")
        td4.innerText = data[x]["description"];
        let td5 = document.createElement("td")
        td5.innerText = data[x]["life_card"];
        life_img_attack.appendChild(td3)
        life_img_attack.appendChild(td4)
        life_img_attack.appendChild(td5)

        table.appendChild(mp_title)
        table.appendChild(life_img_attack)

        document.body.appendChild(table)

    }


}