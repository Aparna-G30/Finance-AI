const monthInput = document.getElementById("month-select");

const today = new Date();

monthInput.value =
    `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, "0")}`;
async function loadData() {

    const month = monthInput.value;

    const response = await fetch(
        `http://127.0.0.1:8000/reports/monthly?month_rep=${month}`
    );

    const data = await response.json();
    console.log(data);
    document.getElementById("total-spending").textContent =
        "₹" + data.total_spending;

    document.getElementById("transactions").textContent =
        data.number_of_transactions;

    document.getElementById("average-expense").textContent =
        "₹" + data.average_expense;

    const table = document.getElementById("expense-table");

    table.innerHTML = "";

    

    data.expenses.forEach(expense => {

        table.innerHTML += `
        <tr>
            <td>${expense.merchant}</td>
            <td>${expense.amount}</td>
            <td>${expense.date}</td>
            <td>${expense.category}</td>
        </tr>
        `;
    });

}

loadData();
const form = document.getElementById("expense-form");

form.addEventListener("submit", async function(event){

    event.preventDefault();

    const expense = {

        merchant: document.getElementById("merchant").value,

        amount: Number(
            document.getElementById("amount").value
        ),

        date: document.getElementById("date").value,

        category: document.getElementById("category").value
    };

    const response = await fetch(
        "http://127.0.0.1:8000/expense",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(expense)
        }
    );

    const data = await response.json();

    alert(data.message);

});