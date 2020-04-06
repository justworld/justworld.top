import Vue from 'vue'
import Router from 'vue-router'
import {LoadingBar} from 'iview'
import Index from '@/components/index/Index'

// 公共区域
// import CommonHeader from '@/components/header/CommonHeader';
import SimpleHeader from '@/components/header/SimpleHeader/SimpleHeader'
import CommonFooter from '@/components/footer/CommonFooter'

// 首页
import ArticleContent from '@/components/content/ArticleContent'
import ArticleListContent from '@/components/content/ArticleListContent'
import SearchResultContent from '@/components/content/SearchResultContent'

Vue.use(Router)

let router = new Router({
  mode: 'history',
  scrollBehavior: () => ({ y: 0 }),
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index,
      children: [
        {
          path: '/',
          name: 'index',
          components: {
            header: SimpleHeader,
            content: ArticleListContent,
            footer: CommonFooter
          },
          meta: {
            title: 'just world | 生命值得为之奋斗'
          }
        },
        {
          path: 'article/:articleId',
          name: 'article',
          components: {
            header: SimpleHeader,
            content: ArticleContent,
            footer: CommonFooter
          }
        },
        {
          path: 'articles',
          name: 'articles',
          components: {
            header: SimpleHeader,
            content: ArticleListContent,
            footer: CommonFooter
          },
          meta: {
            title: '文章 | just world | 生命值得为之奋斗'
          }
        },
        {
          path: 'articles/search',
          name: 'search',
          components: {
            header: SimpleHeader,
            content: SearchResultContent,
            footer: CommonFooter
          },
          meta: {
            title: '搜索 | just world | 生命值得为之奋斗'
          }
        }
      ]
    }
  ]
})

// 配置加载进度条
LoadingBar.config({
  color: '#5cb85c',
  failedColor: '#f0ad4e',
  height: 2
})

router.beforeEach((to, from, next) => {
  LoadingBar.start()
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})

router.afterEach((to, from, next) => {
  LoadingBar.finish()
  window.scrollTo(0, 0)
})

export default router
