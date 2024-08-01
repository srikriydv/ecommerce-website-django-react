import { useState } from "react";
import { Routes, Route } from "react-router-dom";
// Website
import Header from "./components/Header.jsx";
import Home from "./components/Home.jsx";
import Footer from "./components/Footer.jsx";
import Categories from "./components/Categories.jsx";
import CatagoryProducts from "./components/CatagoryProducts.jsx";
import AllProducts from "./components/AllProducts.jsx";
import ProductDetail from "./components/ProductDetail.jsx";
import Checkout from "./components/Checkout.jsx";
// Customer Panel
import Register from "./components/Customer/Register.jsx";
import Login from "./components/Customer/Login.jsx";
import Dashboard from "./components/Customer/Dashboard.jsx";
import Orders from "./components/Customer/Orders.jsx";
import OrderSuccess from "./components/OrderSuccess.jsx";
import OrderFailure from "./components/OrderFailure.jsx";

function App() {
  const [count, setCount] = useState(0);
  return (
    <>
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/categories" element={<Categories />} />
          <Route path="/category/:category_slug/:category_id" element={<CatagoryProducts />} />
          <Route path="/products" element={<AllProducts />} />
          <Route path="/product/:product_slug/:product_id" element={<ProductDetail/>} />
          <Route path="/checkout" element={<Checkout/>} />
          <Route path="/order/success" element={<OrderSuccess />} />
          <Route path="/order/failure" element={<OrderFailure />} />
          <Route path="/customer/register" element={<Register/>} />
          <Route path="/customer/login" element={<Login/>} />
          <Route path="/customer/dashboard" element={<Dashboard />} />
          <Route path="/customer/orders" element={<Orders />} />
        </Routes>
      <Footer />
    </>
  );
}

export default App;
