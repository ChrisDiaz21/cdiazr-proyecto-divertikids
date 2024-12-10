const cart = [];
const totalDisplay = document.getElementById('total');

function changeProductQuantity(name, amount) {
  const priceMapping = { 'Producto 1': 15.00, 'Producto 2': 19.99, 'Producto 3': 9.99 };
  const quantityElement = document.getElementById(`${name}-quantity`);
  let quantity = parseInt(quantityElement.textContent) || 0;
  quantity = Math.max(0, quantity + amount);
  quantityElement.textContent = quantity;

  if (quantity > 0) {
    addToCart(name, priceMapping[name], quantity);
  } else {
    removeFromCart(name);
  }
}

function addToCart(name, price, quantity) {
  const itemIndex = cart.findIndex(item => item.name === name);
  if (itemIndex > -1) {
    cart[itemIndex].quantity = quantity;
  } else {
    cart.push({ name, price, quantity });
  }
  updateTotal();
}

function removeFromCart(name) {
  const itemIndex = cart.findIndex(item => item.name === name);
  if (itemIndex > -1) {
    cart.splice(itemIndex, 1);
    updateTotal();
  }
  document.getElementById(`${name}-quantity`).textContent = 0;
}

function removeProduct(name) {
  removeFromCart(name);
}

function updateTotal() {
  let total = 0;
  cart.forEach(item => {
    total += item.price * item.quantity;
  });
  totalDisplay.textContent = total.toFixed(2);
}

function handleBuy() {
  alert('¡Gracias por tu compra! El total es $' + totalDisplay.textContent);
}
