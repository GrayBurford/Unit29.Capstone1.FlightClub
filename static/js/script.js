
// let buttons = Array.from(document.querySelectorAll('button')).filter(button => button.id !== 'search-button');
// // input:not('[type=hidden]')

// let flightData = {
//     airlineName : "",
//     airlineIataCode : "",
//     flightNumber : "",
//     departureDate : "",
//     departureTime : "",
//     departureAirportCode : "",
//     arrivalDate : "",
//     arrivalTime : "",
//     arrivalAirportCode : "",
//     nonstop : true
// }
// console.log(flightData)
// console.log('^--- flightData before click')

// for (let btn of buttons) {
//     btn.addEventListener('click', handleClick);
// }

// function handleClick (event) {
//     flightData.airlineName = event.target.dataset.airlineName;
//     flightData.airlineIataCode = event.target.dataset.airlineIataCode;
//     flightData.flightNumber = event.target.dataset.flightNumber;
//     flightData.departureDate = event.target.dataset.departureDate;
//     flightData.departureTime = event.target.dataset.departureTime;
//     flightData.departureAirportCode = event.target.dataset.departureAirportCode;
//     flightData.arrivalDate = event.target.dataset.arrivalDate;
//     flightData.arrivalTime = event.target.dataset.arrivalTime;
//     flightData.arrivalAirportCode = event.target.dataset.arrivalAirportCode;
//     flightData.nonstop = event.target.dataset.nonstop;
//     // flightData.nonstop = event.target.getAttribute('data-nonstop');
    
//     console.log(flightData)
//     console.log('^--- flightData AFTER click')

//     sendData(flightData);
// }

// async function sendData (flightData) {
//   let response = await axios.post('/saveflight', flightData)
//   console.log(response)
//   console.log(response.data)
//   console.log('^-- flightData as axios response.')
// }



// const originInput = document.getElementById("origin-input");
// const originOptions = document.getElementById("origin-options");
// const destinationInput = document.getElementById("destination-input");
// const destinationOptions = document.getElementById("destination-options");
// const flightTypeSelect = document.getElementById("flight-type-select");
// const departureDateInput = document.getElementById("departure-date-input");
// const returnDate = document.getElementById("return-date");
// const returnDateInput = document.getElementById("return-date-input");
// const travelClassSelect = document.getElementById("travel-class-select");
// const adultsInput = document.getElementById("adults-input");
// const childrenInput = document.getElementById("children-input");
// const infantsInput = document.getElementById("infants-input");
// const searchButton = document.getElementById("search-button");

// const reset = () => {
//   originInput.value = "";
//   destinationInput.value = "";
//   flightTypeSelect.value = "one-way";
//   departureDateInput.valueAsDate = new Date();
//   returnDateInput.valueAsDate = new Date();
//   returnDate.classList.add("d-none");
//   travelClassSelect.value = "ECONOMY";
//   adultsInput.value = 1;
//   childrenInput.value = 0;
//   infantsInput.value = 0;
//   searchButton.disabled = true;
// };

// document.body.addEventListener("change", () => {
//   searchButton.disabled = !originInput.value || !destinationInput.value;
// });

// originInput.addEventListener("input", () => {
//   // autocomplete
// });

// destinationInput.addEventListener("input", () => {
//   // autocomplete
// });

// flightTypeSelect.addEventListener("change", () => {
//   if (flightTypeSelect.value === "one-way") {
//     returnDate.classList.add("d-none");
//   } else {
//     returnDate.classList.remove("d-none");
//   }
// });

// searchButton.addEventListener("click", async () => {
//   // search
// });

// reset();