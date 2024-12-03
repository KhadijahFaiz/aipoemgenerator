<template>
    <div class="poem-history-view">
      <h1>Poem History</h1>
      <PoemHistoryList />
    </div>
  </template>
  
  <script>
  import PoemHistoryList from '@/components/PoemHistoryList.vue'
  
  export default {
    name: 'PoemHistory',
    components: {
      PoemHistoryList
    }
  }
  </script>