<template>
  <div>
    <div v-for="item in article" :key="item.id" class="article">
      <div class="article__main">
        <div class="aricle__title">
          {{item.title}}
        </div>
        <div class="aricle__body">
          {{item.excerpt}}
        </div>
        <div class="aricle__url">
          {{item.link}}
        </div>
      </div>
      <div class="article__end">
        <span class="delete"></span>
      </div>
    </div>
  </div>
</template>
<script>
export default {
    data() {
      return {
        article: []
      }
    },
    mounted() {
      const url = 'https://scrape-b2b08.firebaseio.com/data.json';
      this.$axios.$get(url)
      .then(res => {
        const list = [];

        //最新の結果だけ取得する
        let targetData = '00000000000000';
        let pk = '';
        let date = '';

        for(const key in res) {
          if(res[key] > targetData) {
             targetData = res[key];
             pk = key;
             date = Object.keys(targetData)
          }
        }

        let count = 0;
        const article = targetData[date];
        for(const index in article) {
          this.article.push({
            id:pk + '_' + count,
            title: article[index].title,
            link: article[index].link,
            excerpt: article[index].excerpt,
          })
          count++;
        }
      })
      .catch(res=>console.log(res))
    }
}
</script>
<style scoped>
  .article {
    font-size:0.7rem;
    border:1px solid;
    margin:10px;
    padding:10px;
    display: flex;
    align-items: center;
  }
</style>
