<script lang="ts">
	import ContextMenu from "$lib/ContextMenu.svelte";
	import { onMount } from "svelte";
	import type { Context } from '$lib/ContextInterface';
    let context: Context = {name: "nothing"};
</script>

<meta name="viewport" content="width=device-width, initial-scale=1"/>

<body>
    <div class="navbar-container">
        <div class="navbar-proj-title">
            Project Title
        </div>
        <div class="navbar-profile">
            profile
        </div>
    </div>
    <div class="navbar-container">
        <div class="navbar-page-text">page 1</div>
        <div class="navbar-page-text">page 2</div>
        <div class="navbar-page-text">page 3</div>
        <div class="navbar-page-text">page 4</div>
    </div>

    <div class="homepage-first-section">
        <article class="notification-container">
            <h1 class="section-title" id="notification">Notifications</h1>
                <article class="notification-card" on:contextmenu={() => {context={name: "notification_1"}}}>
                    <div class="notification-heading-container">
                        <h3 class="notification-title-text">
                            Notification 1
                        </h3>
                        <div class="notification-timestamp-container">
                            <div class="notification-last-updated-container">
                                Last updated
                            </div>
                            <div class="notification-published-container">
                                Published date
                            </div>
                        </div>
                    </div>
                    
                    <div class="grid" id="notification-info-container">
                        <div class="notification-type-container" id="notification-type-1">Type 1</div>
                        <div class="notification-urgency-container" id="notification-urgency-1">Urgency 1</div>
                        <div class="notification-status-container" id="notification-status-1">
                            Status 1
                        </div>
                    </div>
                    <div class="notification-summary-container">
                        <div class="notification-who-container">
                            Who responsible
                        </div>
                        <div class="notification-where-container">
                            Where issue
                        </div>
                    </div>
                </article>
    
                <article class="notification-card" on:contextmenu={() => {context={name: "notification_2"}}}>
                    <div class="notification-heading-container">
                        <h3 class="notification-title-text">
                            Notification 2
                        </h3>
                        <div class="notification-timestamp-container">
                            <div class="notification-last-updated-container">
                                Last updated
                            </div>
                            <div class="notification-published-container">
                                Published date
                            </div>
                        </div>
                    </div>
                    
                    <div class="grid" id="notification-info-container">
                        <div class="notification-type-container" id="notification-type-2">Type 2</div>
                        <div class="notification-urgency-container" id="notification-urgency-2">Urgency 2</div>
                        <div class="notification-status-container" id="notification-status-2">
                            Status 2
                        </div>
                    </div>
                    <div class="notification-summary-container">
                        <div class="notification-who-container">
                            Who responsible
                        </div>
                        <div class="notification-where-container">
                            Where issue
                        </div>
                    </div>
                </article>
    
                <article class="notification-card" on:contextmenu={() => {context={name: "notification_3"}}}>
                    <div class="notification-heading-container">
                        <h3 class="notification-title-text">
                            Notification 3
                        </h3>
                        <div class="notification-timestamp-container">
                            <div class="notification-last-updated-container">
                                Last updated
                            </div>
                            <div class="notification-published-container">
                                Published date
                            </div>
                        </div>
                    </div>
                    
                    <div class="grid" id="notification-info-container">
                        <div class="notification-type-container" id="notification-type-3">Type 3</div>
                        <div class="notification-urgency-container" id="notification-urgency-3">Urgency 3</div>
                        <div class="notification-status-container" id="notification-status-3">
                            Status 3
                        </div>
                    </div>
                    <div class="notification-summary-container">
                        <div class="notification-who-container">
                            Who responsible
                        </div>
                        <div class="notification-where-container">
                            Where issue
                        </div>
                    </div>
                </article>
        </article>
    
    
        <article class="work-request-section-container">
            <h1>Work Requests</h1>
            <article class="work-request-card">
                <div class="wr-header">
                    <div class="wr-top-left-container">
                        <h1 class="wr-title-text">ID #1234</h1>
                    </div>
                    
                    <div class="wr-top-right-container">
                        <div class="wr-priority-container" id="wr-priority-type-1">URGENT</div>
                        <div class="wr-published-date-container">Submitted: 09/15/2023 at 1:30 PM</div>
                    </div>
                </div>
                <div class="wr-summary-container">
                    <div class="wr-subheading-container">
                        <div class="wr-type-container" id="wr-type-reactive">Reactive Maintenance</div>
                        <div class="wr-type-reactive-subheading-bottom">
                            <div class="wr-asset-container" id="wr-asset-type-1">Elevator</div>
                            <div class="wr-location-container">Floor 7, Room 303</div>
                        </div>
                    </div>
                    <div class="wr-issue-container">
                        <div class="wr-issue-title-text">Issue:</div>
                        Elevator doors stuck open. Unsure what caused the issue. Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum Loreum Ipsum. </div>
                    
                </div>
                <div class="wr-review-container">
                    <button class="wr-review-button">
                        Review
                    </button>
                </div>
            </article>
        </article>
    </div>

    <div class="homepage-second-section">
        <div class="current-trends-container">
            <h1 class="ct-title-text">Current Trends</h1>
            <details class="ct-mt-container" open>
                <summary role="button" class="ct-mt-title-text">
                    Maintenance History and Forecast
                </summary>
                <div class="ct-mt-container">
                    <img src="https://charts.livegap.com/2020/images/paper-en.png" class="ct-mt-image"/>
                </div>
            </details>

            <details class="ct-wr-container">
                <summary role="button" class="ct-wr-title-text">
                    Work Request History and Forecast
                </summary>
                <div class="ct-wr-container">
                    <img src="https://charts.livegap.com/2020/images/paper-en.png" class="ct-mt-image"/>
                </div>
            </details>

            <details class="ct-mt-container">
                <summary role="button" class="ct-ot-title-text">
                    Some other trend
                </summary>
                <div class="ct-mt-container">
                    <img src="https://charts.livegap.com/2020/images/paper-en.png" class="ct-mt-image"/>
                </div>
            </details>
        </div>
    </div>

    <div class="homepage-third-section">
        Third section
    </div>

    <ContextMenu bind:context/>
    
</body>

<style>
    /* components */
    article {
        border-radius: 5px;
        border-style: solid;
    }

    body {
        background-color: white;
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
        /* padding-bottom: 20px; */
    }

    .navbar-page-text:hover {
        font-weight: bold;
        cursor: pointer;
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

    .notification-last-updated-container {
        /* background-color: blue; */
        /* width: 25%; */
        display: flex;
        justify-content: right;
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
        background-color: white;
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

    #wr-asset-type-1 {
        background-color: #3083DC;
    }

    #wr-priority-type-1{
        background-color: #EF5B5B;
        color: white;
    }

    #notification-type-3, #notification-urgency-3, #notification-status-3 {
        background-color: #EF5B5B;
        border-style: none;
        box-shadow: 2px 2px 2px 0px rgba(0, 0, 0, 0.25);
    }

    #notification-info-container {
        /* border-style: solid; */
        /* width: 25%; */
    }
</style>