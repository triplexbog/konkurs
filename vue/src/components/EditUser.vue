<template>
  <div class="login-form-container">
    <h2>Вход</h2>
    <form @submit.prevent="login" class="login-form">
      <div class="form-group">
        <label for="login" class="form-label">Логин:</label>
        <input type="text" v-model="userData.login" class="form-input" required>
      </div>
      <div class="form-group">
        <label for="password" class="form-label">Пароль:</label>
        <input type="password" v-model="userData.password" class="form-input" required>
      </div>
      <button type="submit" class="submit-button">Войти</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userData: {
        login: '',
        password: ''
      }
    };
  },
  methods: {
    login() {
      fetch('http://localhost:8000/api/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.userData)
      })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        if (data.success) {
          console.log('Авторизация прошла успешно');
          
        } else {
          console.error('Ошибка при авторизации');
        
        }
      });
    }
  }
};
</script>

<style scoped>
.login-form-container {
  text-align: center;
}

.login-form {
  max-width: 300px;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 15px;
}

.form-label {
  display: block;
  margin-bottom: 5px;
}

.form-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.submit-button {
  background-color: blue;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}
</style>
