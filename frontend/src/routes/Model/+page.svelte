<script>
	import ModelPage from "$lib/Model_Page.svelte";

</script>

<body>
    <div class="navbar-container">
        <div class="navbar-proj-title">
            Model Maintenance
        </div>
        <div class="navbar-profile">
            <img  class="navbar-profile-img" src="https://samanthabrandon.com/wp-content/uploads/2023/04/sam-.png"/>
        </div>
    </div>
    <div class="navbar-container">
        <div class="navbar-page-text"><a href="/" class="q">Dashboard</a></div>
        <div id="nb-active">3D Map</div>
        <div class="navbar-page-text">Work Orders</div>
        <div class="navbar-page-text">Work Requests</div>
    </div>
    <ModelPage/>
</body>

<style>
        /* components */
        article {
        border-radius: 5px;
        border-style: solid;
    }

    body {
        background-color: white;
        overflow-x:hidden;
        /* overflow-y:hidden; */
    }

    .q{
        color: white;
    }

    .q:hover{
        font-weight: bold;
        text-decoration: none;
    }

    /* class */
    .section-title {
        
    }

    .grid {
        /* background-color: red; */
        /* width: 100%; */
        justify-content: left;
        align-items: center;
        display: flex;

    }

    .navbar-container {
        /* border-style: solid; */
        width: 100%;
        display: flex;
        justify-content: center;
        padding-left: 10px;
        padding-right: 10px;
        height: 70px;
        background-color: #0B132B;
    }

    .navbar-proj-title{
        /* border-style: solid; */
        width: 90%;
        text-align: left;
        color: white;
        font-weight: bold;
        margin-top: 20px;
        padding-left: 2%;
        font-size: 25px;
    }

    .calendar-times-and-events-calendar{
        /* background-color: red; */
        /* z-index: 0; */
        margin-top: 75px;
    }


    .calendar-days{
        display: flex;
        position: absolute;
        padding-left: 475px;
        z-index: 0;
    }

    .calendar-day-text{
        padding: 10px;
        border-style: solid;
        border-color: grey;
        border-width: 1px;
        height: 1075px;
        width:100px;
        text-align: center;
    }

    .navbar-profile{
        /* border-style: solid; */
        width: 10%;
        display: flex;
        justify-content: right;
        margin-top: 20px;
        padding-right: 2%;
        color: #edf0f3;
    }

    .homepage-first-section{
        border-style: solid;
        /* border-color: red; */
        display: flex;
    }

    .navbar-page-text {
        color: #edf0f3;
        width: 100%;
        display: flex;
        justify-content: center;
        font-weight: 200;
        margin-top: 20px;
        padding-top: 5px;
        /* border-style: solid; */
        /* padding-bottom: 20px; */
    }

    .navbar-page-text:hover {
        font-weight: bold;
        cursor: pointer;
        text-decoration: none;
    }

    .current-trends-container{
        /* width: 75%;
        justify-content: center; */
    }

    .work-request-section-container{
        width: 40%;
        background-color: #0B132B;
        border-radius: 10px;
    }

    .navbar-proj-title:hover{
        cursor: pointer;
    }

    .navbar-profile:hover{
        cursor: pointer;
    }

    .wr-top-left-container{
        /* border-style: solid; */
        border-color: red;
        width: 65%;
    }

    #nb-active{
        background-color: #152041;
        font-weight: 500;
        width: 100%;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .navbar-profile-img{
        border-radius: 50%;
        height: 65px;
    }

    .calendar-container{
        border-style: solid;
        position: relative;
        overflow: scroll;
        height: 100%;
    }

    .calendar-month-name{
        font-size: 42px;
        font-weight: bold;
        padding-left: 20px;
        padding-bottom: 10px;
    }

    .calendar-row{
        border-top: solid;
        border-bottom: solid;
        display: flex;
        z-index: 10;
        position: absolute;
        height: 250px;
        /* width: 150%; */
        /* background-color: red; */
    }

    #dashboard-text{
        background-color: red;
        /* height: 50px; */
        /* margin-bottom: -10px; */
    }

    .cr-event-name{
        /* border-right: solid grey; */
        width:475px;
        display: flex;
        text-align: center;
        justify-content: center;
        align-items: center;
        font-size: 35px;
        font-weight: bold;
        margin-right: 10px;
    }

    .cr-event-content{
        border-style: solid;
        border-radius: 15px;
        padding-left: 10px;
        padding-right: 10px;
        color: white;
        margin-top: 10px;
        margin-bottom: 10px;
        z-index: 99;
    }


    .notification-container {
        /* background-color: white; */
        border-radius: 15px;
        border-style: none;
        margin-left: 5%;
        background-color: #0B132B;
        margin-right: 5%;
    }

    .notification-title-text {
        color: black;
    }

    .notification-type-text {
        color: black;
    }

    .notification-card {
        background-color: white;
        border-style: none;
        border-radius: 10px;
    }

    .wr-top-right-container{
        width: 45%;
        /* border-style: solid; */
        text-align: right;
    }

    .notification-type-container, .notification-urgency-container, .notification-status-container {
        border-style: solid;
        border-radius: 15px;
        /* width: 25%; */
        text-align: center;
        margin-top: 10px;
        margin-bottom: 10px;
        color: white;
        font-weight: bold;
        font-size: 95%;
        padding-top: 3px;
        padding-bottom: 3px;
        padding-left: 30px;
        padding-right: 30px;
    }

    .notification-summary-container {
        /* border-style: solid; */
        display: flex;
        color: black;
        margin-top: 15px;
        display: flex;
        justify-content: center;
    }

    .notification-where-container {
        /* border-style: solid; */
        width: 75%;
    }

    .notification-who-container {
        /* border-style: solid; */
        width: 25%;
    }

    .notification-published-container{
        /* border-style: solid; */
        /* width: 33%; */
        color: rgb(80, 80, 80);
        font-size: 13px;
    }

    .notification-timestamp-container {
        /* border-style: solid; */
        /* border-color: green; */
    }

    .notification-heading-container {
        /* background-color: purple; */
        display: flex;
        /* border-style: solid; */
        /* height: 6vh; */
    }

    .notification-text{
        color: black;
        border-style: solid;
        border-width: 1px;
        border-radius: 5px;
        padding: 7px;
        box-shadow: 1px 1px 1px 1px rgba(0, 0, 0, 0.5);
    }

    .notification-text-title{
        font-weight: 500;
    }

    .notification-last-updated-container {
        /* background-color: blue; */
        /* width: 25%; */
        display: flex;
        justify-content: right;
        text-align: right;
        color: black;
        font-size: 20px;
    }

    .work-order-section-container{
        border-style: none;

    }

    .notification-card:hover {
        cursor:pointer;
    }

    .wr-header{
        /* border-style: solid; */
        display: flex;
        width:100%;
    }

    .wr-title-text{
        /* border-style: solid; */
        border-color: purple;
        /* width: 75%; */
        color: black;
    }

    .notification-container {
        width: 45%;
    }

    .work-request-card{
        background-color: white;
        color: black;
        border-style: none;
    }

    .wr-summary-container{
        /* background-color: white; */
        border-radius: 5px;
        padding: 2%;
    }

    .wr-review-container{
        /* border-style: solid; */
        display: flex;
        justify-content: center;
    }

    .wr-review-button{
        background-color:#3083DC;
        border-radius: 5px;
        border-style: none;
        width: 90%;
        box-shadow: 2px 2px 5px 2px rgba(0, 0, 0, 0.25);
    }

    .wr-review-button:hover{
        background-color:#2661a0;
        font-weight: bold;
    }

    .wr-published-date-container{
        color:black;
        width: 100%;
        padding-right: 11px;
        /* border-style: solid; */
    }

    .wr-subheading-container{
        /* display: flex; */
        /* border-style: solid; */
        padding: 10px;
        border-radius: 10px;
        /* box-shadow: 1px 1px 1px 2px rgba(0, 0, 0, 0.5); */
        align-items: center;
        justify-content: center;
    }

    .wr-asset-container, .wr-priority-container, .wr-type-container{
        color: white;
        /* background-color: #EF5B5B; */
        border-radius: 20px;
        text-align: center;
        font-weight: 500;
        padding-top: 5px;
        padding-bottom: 5px;
    }

    .wr-asset-container{
        width: 45%;
        /* margin-left: 20px; */
    }

    .wr-location-container{
        width: 45%;
        border-radius: 20px;
        text-align: center;
        font-weight: 500;
        padding-top:5px;
        padding-bottom: 5px;
        background-color:#FFBA49;
        margin-left: 20px;
    }

    .wr-type-container{
        width: 100%;
        border-radius: 20px;
        text-align: center;
        font-weight: 500;
        padding-top:5px;
        padding-bottom: 5px;
        background-color:#FFBA49;
        /* margin-left: 20px; */
        margin-bottom: 5px;
    }

    .wr-type-reactive-subheading-bottom{
        display: flex;
        /* border-style: solid; */
        align-items: center;
        justify-content: center;
    }

    .wr-issue-container{
        color: black;
    }

    .wr-priority-container{
        color: black;
    }

    .wr-location-container{
        color:white;
    }

    .wr-budget-container{
        color: black;
    }

    .work-order-card{
        background-color: white;
        border-radius: 10px;
        border-style: none;
    }
    
    .notification-title-text {
        width: 75%;
    }

    .wr-issue-container{
        border-style: solid;
        border-radius: 10px;
        padding: 15px;
        max-height: 150px;
        /* min-height: 100px; */
        overflow:scroll;
        overflow-x:hidden;
        border-color:#b6b6b6;
    }

    .wr-issue-title-text{
        font-weight: bold;
    }

    .wr-issue-container::-webkit-scrollbar{
        background: transparent;
    }

    .notification-card:hover{
        background-color: #dbdbdb;
    }

    .work-request-card:hover{
        background-color: #dbdbdb;
 
    }

    .homepage-second-section {
        color: black;
        background-color: #0B132B;
        padding: 15px;
        /* border-radius: 5px;; */
    }

    .ct-title-text{
        color: white;
        /* font-size: 30px; */
        font-weight: bold;
        text-align: center;
        padding-top: 30px;
    }

    .ct-mt-container, .ct-wr-container{
        background-color: white;
        border-radius: 15px;
    }

    .ct-mt-title-text, .ct-wr-title-text{
        font-size: 25px;
        font-weight: 600;
        border-style: solid;
        text-align: center;
    }

    .ct-wr-title-text{
        background-color: #0068BE;
    }

    .ct-ot-title-text{
        background-color: #004FA0;
        font-size: 25px;
        font-weight: 600;
        border-style: solid;
        text-align: center;
    }

    .ct-mt-image, .notification-where-container{
        /* border-style: solid; */
        width: 100%;
    }

    .homepage-third-section{
        height: 50vh;
        color: black;
        padding-top: 50px;
    }
    

    @media only screen and (max-width: 1375px){
        .notification-container {
            width: 100%;
            margin-left: 0%;
            /* background-color: red; */
        }

        .wr-subheading-container{
            display:block;
            /* border-style: solid; */
        }

        .wr-type-container, .wr-asset-container, .wr-location-container{
            width: 100%;
            margin-top: 10px;
            margin-left: 0px;
        }

        .homepage-first-section{
            display: block;
        }
        
        .work-request-section-container{
            width: 100%;
        }
    }

    /* IDs */
    #notification-type-1, #notification-urgency-1, #notification-status-1 {
        background-color: #317B22;
        border-style: none;
        box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
    }

    #notification-status-4 {
        background-color: #317B22;
        border-style: none;
        box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
        margin-left: 10px;
    }

    #notification-status-5 {
        background-color: #FFBA49;
        border-style: none;
        box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
        margin-left: 10px;
    }

    #notification-status-6 {
        background-color: #EF5B5B;
        border-style: none;
        box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
        margin-left: 10px;
    }

    #notification-type-1, #notification-urgency-1, #notification-status-1 {
        background-color: #317B22;
        border-style: none;
        box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
    }

    #notification-type-2, #notification-urgency-2, #notification-status-2 {
        background-color: #FFBA49;
        border-style: none;
        box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
    }

    #wr-type-reactive{
        background-color: #EF5B5B;
        text-align: center;
        color: white;
        font-weight: bold;
    }

    #wr-type-preventative{
        background-color: #FFBA49;
        text-align: center;
        color: white;
        font-weight: bold;
    }

    #wr-asset-type-1 {
        background-color: #3083DC;
    }

    #cr-event-1-parent{
        background-color:#EF5B5B;
        border-style: solid;
        border-color:#EF5B5B;
        width: 580px;
        /* width: 735px; */
    }

    #cr-event-2-parent{
        background-color:#3083DC;
        border-style: solid;
        border-color:#3083DC;
        width: 1170px;
        margin-left: 200px;
        /* width: 735px; */
    }

    #cr-event-3-parent{
        background-color:#FFBA49;
        border-style: solid;
        border-color:#FFBA49;
        width: 975px;
        margin-left: 900px;
        /* width: 735px; */
    }

    #cr-event-4-parent{
        background-color:#317B22;
        border-style: solid;
        border-color:#317B22;
        width: 975px;
        margin-left: 100px;
        /* width: 735px; */
    }

    #cr-event-1-c1 {
        background-color: #EF5B5B;
        border-style: solid;
        border-color: #EF5B5B;
        width: 180px;
        margin-left: 0px;
    }

    #cr-event-2-c1 {
        background-color: #3083DC;
        border-style: solid;
        border-color: #3083DC;
        width: 180px;
        margin-left: 200px;
    }

    #cr-event-2-c2 {
        background-color: #3083DC;
        border-style: solid;
        border-color: #3083DC;
        width: 685px;
        margin-left: 395px;
    }

    #cr-event-2-c3 {
        background-color: #3083DC;
        border-style: solid;
        border-color: #3083DC;
        width: 190px;
        margin-left: 1093px;
    }

    #cr-event-2-c4 {
        background-color: #3083DC;
        border-style: solid;
        border-color: #3083DC;
        width: 180px;
        margin-left: 1294px;
    }

    #cr-1 {
        /* margin-top: 225px; */
        border-top: solid;
        border-width: 1px;
        width: 2575px;
        /* margin-bottom: 50px; */
        /* border-color: purple; */
    }
    

    #cr-2 {
        margin-top: 250px;
        border-bottom: solid;
        border-width: 1px;
        width: 2575px;        /* margin-bottom: 50px; */
        /* border-color: purple; */
    }

    #cr-3 {
        margin-top: 500px;
        border-bottom: solid;
        border-width: 1px;
        /* border-color: purple; */
        /* padding-bottom: 500px; */
        /* height: 500px; */
        border-style: solid;
        width: 2575px;        /* margin-bottom: 50px; */
        /* border-color: purple; */
    }

    #cr-4 {
        margin-top: 750px;
        border-bottom: solid;
        border-width: 1px;
        width: 2575px;        /* margin-bottom: 50px; */
        /* border-color: purple; */
    }

    #cr-event-1-c2 {
        background-color: #EF5B5B;
        border-style: solid;
        border-color: #EF5B5B;
        width: 280px;
        margin-left: 200px;
    }

    #cr-event-1-c3 {
        background-color: #EF5B5B;
        border-style: solid;
        border-color: #EF5B5B;
        width: 95px;
        margin-left: 493px;
        font-size: 14px;
    }

    #cr-event-3-c1 {
        background-color: #FFBA49;
        border-style: solid;
        border-color: #FFBA49;
        width: 280px;
        margin-left: 900px;
    }

    #cr-event-3-c2 {
        background-color: #FFBA49;
        border-style: solid;
        border-color: #FFBA49;
        width: 280px;
        margin-left: 1200px;
    }
    #cr-event-3-c3 {
        background-color: #FFBA49;
        border-style: solid;
        border-color: #FFBA49;
        width: 180px;
        margin-left: 1495px;
    }

    #cr-event-3-c4 {
        background-color: #FFBA49;
        border-style: solid;
        border-color: #FFBA49;
        width: 175px;
        margin-left: 1700px;
    }

    #cr-event-4-c1 {
        background-color: #317B22;
        border-style: solid;
        border-color: #317B22;
        width: 280px;
        margin-left: 200px;
    }

    #cr-event-4-c2 {
        background-color: #317B22;
        border-style: solid;
        border-color: #317B22;
        width: 280px;
        margin-left: 500px;
    }

    #cr-event-4-c3 {
        background-color: #317B22;
        border-style: solid;
        border-color: #317B22;
        width: 270px;
        margin-left: 800px;
    }

    #wr-priority-type-1{
        background-color: #EF5B5B;
        color: white;
    }

    #wr-priority-type-2{
        background-color: #317B22;
        color: white;
    }

    #notification-type-3, #notification-urgency-3, #notification-status-3 {
        background-color: #EF5B5B;
        border-style: none;
        box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
    }

    #notification-info-container {
        display: flex;
        justify-content: center;
        /* border-style: solid; */
        /* width: 25%; */
    }
</style>