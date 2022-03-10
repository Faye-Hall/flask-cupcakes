const BASE_URL = "http://127.0.0.1:5000/api";


/** Generate Data to HTML */
function Cupcake_data_to_HTML(cupcake) {
    return `
         <ul>
         <li data-cupcake-id="${cupcake.id}">${cupcake.id}  / ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
        <img class="Cupcake-img"
              src="${cupcake.image}"
              alt="(no image provided)"
              width = "40"
              height = "40">
              <button class="delete-button">Delete</button>
         </li>
         <ul>     
    `;
}


/** put cupcakes from DB on page. */

async function showInitialCupcakes() {
    const response = await axios.get(`${BASE_URL}/cupcakes`);
    for (let each of response.data.all_cupcakes) {
        let cupcake = Cupcake_data_to_HTML(each);
        $("#cupcake-list").append(cupcake)
    }
}



showInitialCupcakes()



$("#new-cupcake-form").on("submit", async function (evt) {
    evt.preventDefault();

    let flavor = $("#flavor").val();
    let rating = $("#rating").val();
    let size = $("#size").val();
    let image = $("#image").val();

    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
        flavor,
        rating,
        size,
        image
    });

    let newCupcake = $(Cupcake_data_to_HTML(newCupcakeResponse.data.new_cupcake));
    z
    $("#cupcake-list").append(newCupcake);
    $("#new-cupcake-form").trigger("reset");
});

$("#cupcake-list").on("click", ".delete-button", async function (evt) {
    evt.preventDefault();
    let $cupcake = $(evt.target).closest("li");
    let cupcakeId = $cupcake.attr("data-cupcake-id");

    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
    $cupcake.remove();
});