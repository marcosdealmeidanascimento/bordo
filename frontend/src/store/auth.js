import { defineStore } from 'pinia';
import axios from 'axios';


const baseUrl = `${import.meta.env.VITE_SERVER_NAME}/users`;

export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    // initialize state from local storage to enable user to stay logged in
    user: JSON.parse(localStorage.getItem('user')),
    token: JSON.parse(localStorage.getItem('token')),
    expires: JSON.parse(localStorage.getItem('expires'))
  }),
  actions: {
    async login(username, password) {
      var data = {
        'grant_type': '',
        'username': username,
        'password': password,
        'scope': '',
        'client_id': '',
        'client_secret': ''
      }
      var config = {
        method: 'post',
        url: import.meta.env.VITE_SERVER_NAME + 'login/access-token',
        headers: {
          'accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: data
      };

      const response = await axios(config);
      // update pinia state
      this.user = response.data.user;
      this.token = response.data.access_token
      this.expires = response.data.expires
      // store user details and jwt in local storage to keep user logged in between page refreshes
      localStorage.setItem('user', JSON.stringify(this.user));
      localStorage.setItem('token', JSON.stringify(this.token));
      localStorage.setItem('expires', JSON.stringify(this.expires));
      // redirect to previous url or default to home page
      window.location.assign("/")

    },
    logout() {
      this.user = null;
      localStorage.removeItem('user');
      localStorage.removeItem('token');
      localStorage.removeItem('expires');
    },
    checkLoginState() {
      const now = Date.now()
      console.log(this.expires > now);

      // if (now >= expiresAt) {
      //   console.log("LogOut");
      // }
    },
  }
});
