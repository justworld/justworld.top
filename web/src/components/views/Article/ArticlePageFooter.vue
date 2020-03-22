<template>
  <div class="article-page-footer">
    <social-section :type="'Article'" :postId="postId"></social-section>
  </div>
</template>

<script type="text/ecmascript-6">
import SocialSection from '@/components/views/Comment/SocialSection'

export default {
  components: {
    'social-section': SocialSection
  },
  props: {
    postId: Number
  }
}
</script>
