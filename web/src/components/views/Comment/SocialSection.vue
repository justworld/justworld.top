<template>
  <div class="social-section">
    <div id="gitalk-container" v-if="show"></div>
    <!--<div id="SOHUCS" :sid="type+postId"></div>-->
  </div>
</template>

<script type="text/ecmascript-6">
import BrowseMore from '@/components/views/BrowseMore'

export default {
  props: {
    type: String,
    postId: Number
  },
  data () {
    return {
      show: null
    }
  },
  components: {
    'browse-more': BrowseMore
  },
  watch: {
    postId (value) {
      this.show = value
      this.$nextTick(() => {
        // eslint-disable-next-line no-undef
        var gitalk = new Gitalk({
          clientID: 'f2393b8acb606af13450',
          clientSecret: '7699945845d24d00ed4832b37687d0d2f3957ebc',
          repo: 'justworld.top',
          owner: 'justworld',
          labels: [this.type],
          admin: ['justworld'],
          id: location.href, // Ensure uniqueness and length less than 50
          distractionFreeMode: false // Facebook-like distraction free mode
        })
        gitalk.render('gitalk-container')
      })
    }
  }
}
</script>
