<template>
  <div class="user-list-container">
    <h2>Регистрация пользователя</h2>
    <form @submit.prevent="registerUser" class="registration-form">
      <div class="form-group">
        <label for="login">Логин:</label>
        <input type="text" v-model="userData.login" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" v-model="userData.email" required>
      </div>
      <div class="form-group">
        <label for="phone">Телефон:</label>
        <input type="tel" v-model="userData.phone" required>
      </div>
      <div class="form-group">
        <label for="firstName">Имя:</label>
        <input type="text" v-model="userData.firstName" required>
      </div>
      <div class="form-group">
        <label for="lastName">Фамилия:</label>
        <input type="text" v-model="userData.lastName" required>
      </div>
      <button type="submit" class="submit-button">Зарегистрироваться</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userData: {
        login: '',
        email: '',
        phone: '',
        firstName: '',
        lastName: ''
      }
    };
  },
  methods: {
    async registerUser() {
      try {
        const response = await fetch('http://localhost:8000/api/register/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.userData)
        });
        if (!response.ok) {
          throw new Error('Ошибка при регистрации пользователя');
        }
        this.userData = {
          login: '',
          email: '',
          phone: '',
          firstName: '',
          lastName: ''
        };
        alert('Пользователь успешно зарегистрирован!');
      } catch (error) {
        console.error(error);
        alert('Ошибка при регистрации пользователя');
      }
    }
  }
};
</script>

<style scoped>
.user-list-container {
  text-align: center;
}

.registration-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input[type="text"],
input[type="email"],
input[type="tel"] {
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
