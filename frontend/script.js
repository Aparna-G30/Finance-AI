let currentExpenses = [];
let editingExpenseId = null;
const monthInput = document.getElementById("month-select");

monthInput.addEventListener(
    "change",
    () => {
        console.log("Month changed");
        loadData();
        loadCategoryData();
    }
);

const today = new Date();

monthInput.value =
    `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, "0")}`;
async function loadData() {

    const month = monthInput.value;
    
    // const selectedCategory=document.getElementById("category-filter").value;
    // console.log(selectedCategory);
    
const response = await fetch(
    `http://127.0.0.1:8000/reports/monthly?month_rep=${month}`
);
if (!response.ok) {
    const error = await response.json();
    alert(error.detail[0].msg);
    return;
}
const data = await response.json();
    currentExpenses = data.expenses;

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
            <td>
                <button onclick="editExpense(${expense.id})">
                    Edit
                </button>

                <button onclick="deleteExpense(${expense.id})">
                    Delete
                </button>
            </td>
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

        category: document.getElementById("category").value,

        // note: document.getElementById("note").value

    };

    if(editingExpenseId === null)
    {

        // CREATE NEW EXPENSE

        await fetch(
            "http://127.0.0.1:8000/expense",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify(expense)
            }
        );
        

    }
    else
    {

        await fetch(
            `http://127.0.0.1:8000/expenses/${editingExpenseId}`,
            {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
            },
            body: JSON.stringify(expense)
            }
        );

        const amountError =
            document.getElementById("amount-error");

        if (expense.amount <= 0) {
            amountError.textContent =
             "Amount must be greater than 0.";

            return;
        }
        amountError.textContent = "";
        editingExpenseId = null;
    }
    // console.log("Restarting form...");
    form.reset();

    const today = new Date().toISOString().split("T")[0];
    console.log(today);

    document.getElementById("date").value = today;

    console.log(document.getElementById("date").value);

    loadData();
});
async function deleteExpense(expenseId){

    await fetch(
        `http://127.0.0.1:8000/expenses/${expenseId}`,
        {
            method: "DELETE"
        }
    );

    loadData();

}

function editExpense(id){

    const expense = currentExpenses.find(
        expense => expense.id === id
    );

    document.getElementById("merchant").value =
        expense.merchant;

    document.getElementById("amount").value =
        expense.amount;

    document.getElementById("date").value =
        expense.date;

    document.getElementById("category").value =
        expense.category;

    // document.getElementById("note").value =
    // expense.note;

    editingExpenseId = id;


}

const categoryFilter =
    document.getElementById("category-filter");

// console.log(document.getElementById("month-select"));
// const monthInput =
//     document.getElementById("month-select");

categoryFilter.addEventListener(
    "change",
    () => {
        console.log("Month changed");
        loadData();
        loadCategoryData();
    }
);
async function loadCategoryData(){

    const category =
        document.getElementById("category-filter").value;

    const month = monthInput.value;

    const response = await fetch(
        `http://127.0.0.1:8000/expenses/filter/month?category=${category}&month_rep=${month}`
    );

    const expenses = await response.json();
    console.log(expenses);
    
    
    const table =
        document.getElementById("category-table");

    let total=0;

    table.innerHTML = "";
    expenses.forEach(expense => {

        total+= expense.amount;
        
        table.innerHTML += `
        <tr>
            <td>${expense.merchant}</td>
            <td>${expense.amount}</td>
            <td>${expense.date}</td>
            <td>${expense.note || "-"}</td>
        </tr>
        `;

    });
    document.getElementById("category-total").textContent =
    "Total: ₹" + total;

    if(category === ""){
    table.innerHTML = "";

    document.getElementById("category-total").textContent =
        "Total: ₹0";
    
    return;
}
document.getElementById("category-transactions").textContent =
        "Transactions: " + expenses.length;


}