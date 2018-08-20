<template>
  <div>
    <section class="hero">
      <figure class="image">
        <img src="~/assets/images/hero.jpg" width="800px">
        <div class="image__title">
          <h1>管理 + 詳細</h1>
        </div>
      </figure>
    </section>
    <div class="wrap">
      <div class="main">
        <section class="section">
          <div class="container">
            <h1 class="title">スクレイピング</h1>
            <h2 class="subtitle">
              <p>スクレイピングは、PythonのBeautifulSoupを使って実施。</p>
              <p>定期的にPyhtonのスクリプトを実行する環境は、サーバを用意してもいいが、AWS Lamdaが安いかもしれない。</p>
            </h2>
          </div>
        </section>
        <section class="section">
          <div class="container">
            <h1 class="title">フロント</h1>
            <h2 class="subtitle">
              <p><strong>Nuxt.js</strong>を使用。管理画面を新規で使うならあり。</p>
              <p>LPサイトに埋め込むjavascriptはどんな感じがよいのだろう。</p>
            </h2>
          </div>
        </section>
        <section class="section">
          <div class="container">
            <h1 class="title">DB + API</h1>
            <h2 class="subtitle">
              Firebaseを使用。Firebaseなら、API用のサーバーいらない気がしてきた。
            </h2>
          </div>
        </section>
      </div>
      <div class="sidebar">
        <div class="section">
          <List />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import List from '@/components/List'

export default {
  components: {
    List
  },
}
</script>

<style>
  .wrap {
    display: flex;
  }

  .main {
    flex:1;
  }

  .image {
    position: relative;
    text-align: center;
  }

  .image__title {
    position: absolute;
    top:53%;
    left:22%;
    font-size:10vw;
    color:white;
  }

  .sidebar {
    min-width: 300px;
    width: 30%;
  }
</style>
