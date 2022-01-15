class Calc {
  constructor() {
    this.operators = document.getElementsByClassName("operator");
    this.numbers = document.getElementsByClassName("number");
    this.input = document.getElementById("id_calc");
    this.backspace = document.getElementById("backspace");
  }

  isLastSpace = () => this.input.value[this.input.value.length - 1] === " ";

  isLastNumber = () => !isNaN(this.input.value[this.input.value.length - 1]);

  isEmpty = () => this.input.value === "";

  numberClickHandler = (event) => {
    event.preventDefault();
    this.input.value += event.target.value;
    console.log(event.target.value);
  };

  operatorClickHandler = (event) => {
    event.preventDefault();
    if (this.isLastSpace()) {
      const splitValue = this.input.value.split("");
      splitValue[this.input.value.length - 2] = event.target.value;

      this.input.value = splitValue.join("");
    } else if (this.isLastNumber()) {
      this.input.value += ` ${event.target.value} `;
    }
  };

  backspaceClickHandler = (event) => {
    event.preventDefault();
    const charToDelete = this.isLastSpace() ? -3 : -1;
    this.input.value = this.input.value.slice(0, charToDelete);
  };

  appendEvents = () => {
    console.log(this);
    [...this.operators].forEach((element) =>
      element.addEventListener("click", this.operatorClickHandler)
    );
    [...this.numbers].forEach((element) =>
      element.addEventListener("click", this.numberClickHandler)
    );
    this.backspace.addEventListener("click", this.backspaceClickHandler);
  };
}

function init() {
  const calc = new Calc();
  calc.appendEvents();
}

document.addEventListener("DOMContentLoaded", init, false);
