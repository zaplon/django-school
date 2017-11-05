<template>
  <div class="animated fadeIn">
    <div class="nav-card card">
        <nav class="nav-table">
          <div class="toolbar">
            <i class="fa fa-plus" data-toggle="modal" data-target="#addTimetable"></i>
          </div>
          <vue-good-table
          :columns="columns"
          :rows="rows"
          :paginate="false"
          styleClass="table table-sm"
          :lineNumbers="false">

          </vue-good-table>
        </nav>
        <main class="nav-main"><full-calendar :events="events"></full-calendar></main>
      </div>
    </div>
</template>
<script>
  import moment from 'moment'

  export default {
    name: 'timetable',
    data () {
      return {
        columns: [
          {
            label: 'Name',
            field: 'name',
            filterable: true
          }
        ],
        rows: [
          {}
        ],
        events: [
          {
            id: 1,
            title: 'event1',
            start: moment().hours(12).minutes(0)
          }
        ]
      }
    },
    methods: {
      addTimetable: () => { alert('qqq') }
    }
  }
</script>

<style>
  @import '~fullcalendar/dist/fullcalendar.css';
</style>
