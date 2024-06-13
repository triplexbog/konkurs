<template>
  <div id="app">
    <button @click="currentPage = 'UserList'">Список пользователей</button>
    <button @click="currentPage = 'FileUpload'">Загрузка файлов</button>
    <button @click="currentPage = 'EditUser'">Загрузка файлов</button>

    <component :is="currentPage" />
  </div>
</template>

<script>
import UserList from './components/UserList.vue';
import FileUpload from './components/FileUpload.vue';
import EditUser from './components/EditUser.vue'

export default {
  name: 'App',
  components: {
    UserList,
    FileUpload,
    EditUser
  },
  data() {
    return {
      currentPage: 'UserList' // начальная страница
    };
  }
}
</script>
