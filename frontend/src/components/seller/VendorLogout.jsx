function SellerLogout(){
    localStorage.removeItem('vendor_login');
    localStorage.removeItem('vendor_username');
    window.location.href='/seller/dashboard';
}
export default SellerLogout;