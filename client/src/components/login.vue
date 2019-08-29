<template>
  <div class="container">
    <h1><img src="../assets/logo.png">
    <br><br>Testing Vue + Flask-login + Flask CORS</h1>

    <div class="tab">
      <button type="button"
        class="btn btn-success btn-sm"
        style="width: 100px; height: 50px; margin: 10px;" v-b-modal.login-modal>Login</button>
      <button type="button"
        class="btn btn-primary"
        style="width: 100px; height: 50px; margin: 10px;">Register</button>
    </div>
      <!-- way to get html directly -->
      <p> <span v-html= this.result></span> </p>
    <b-modal ref="loginModal"
           id="login-modal"
           title="Vue + Flask Login + CORS"
           hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                    label="name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="loginForm.name"
                        required
                        placeholder="Username">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-password-group"
                      label="password:"
                      label-for="form-password-input">
            <b-form-input id="form-password-input"
                          type="password"
                          v-model="loginForm.password"
                          required
                          placeholder="password">
            </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>


<script>
import axios from 'axios';
import querystring from 'querystring';

// axios.defaults.withCredentials = true;

export default {
  name: 'login',
  data() {
    return {
      result: '',
      loginForm: {
        name: '',
        password: '',
      },
    };
  },
  methods: {
    getresults() {
      const path = 'http://localhost:8081/protected';
      axios.get(path)
        .then((res) => {
          this.result = res.data;
        })
        .catch((error) => {
          this.console.error(error);
        });
    },
    login(payload) {
      const path = 'http://localhost:8081/login';
      axios.post(path, querystring.stringify(payload),
        {
          headers:
          {
            'Content-type': 'application/x-www-form-urlencoded',
            'Access-Control-Allow-Headers': 'Set-Cookie',
          },
        })
        .then((res) => {
          this.result = res.data;
        })
        .catch((error) => {
          this.console.log(error);
        });
    },
    initForm() {
      this.loginForm.name = '';
      this.loginForm.password = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.loginModal.hide();
      const payload = {
        name: this.loginForm.name,
        password: this.loginForm.password,
      };
      this.login(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.loginModal.hide();
      this.initForm();
    },
  },
  created() {
  },
};
</script>
