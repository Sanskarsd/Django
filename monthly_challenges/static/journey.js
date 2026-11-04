/* ============================================================
   MONTHLY CHALLENGES
   JOURNEY ENGINE
============================================================ */

document.addEventListener("DOMContentLoaded", () => {


    const robot =
        document.getElementById("journeyRobot");

    const journey =
        document.getElementById("challengeJourney");


    if (!robot) {
        return;
    }


    /* ========================================================
       HEADER
    ======================================================== */

    const header =
        document.querySelector(".site-header");


    const updateHeader =
        () => {

            if (window.scrollY > 50) {

                header.classList.add("scrolled");

            } else {

                header.classList.remove("scrolled");

            }

        };


    window.addEventListener(
        "scroll",
        updateHeader,
        { passive: true }
    );


    updateHeader();



    /* ========================================================
       REVEAL OBSERVER
    ======================================================== */

    const revealElements =
        document.querySelectorAll(".reveal");


    const revealObserver =
        new IntersectionObserver(

            entries => {

                entries.forEach(entry => {

                    if (entry.isIntersecting) {

                        entry.target.classList.add(
                            "visible"
                        );

                    }

                });

            },

            {
                threshold: 0.12
            }

        );


    revealElements.forEach(element => {

        revealObserver.observe(element);

    });



    /* ========================================================
       MONTH STAGES
    ======================================================== */

    const stages =
        document.querySelectorAll(".month-stage");


    if (!journey || stages.length === 0) {

        /*
         * We are probably on challenge.html.
         * Robot can still perform a subtle idle animation.
         */

        robot.classList.add("active");

        robot.style.left = "80%";
        robot.style.top = "70%";

        return;

    }



    /* ========================================================
       JOURNEY STATE
    ======================================================== */

    let currentX = 0;
    let currentY = 0;

    let targetX = 0;
    let targetY = 0;

    let targetAngle = 0;
    let currentAngle = 0;

    let activeStage = -1;

    let ticking = false;



    /* ========================================================
       GET STAGE POSITIONS
    ======================================================== */

    function getStagePositions() {

        const journeyRect =
            journey.getBoundingClientRect();

        const positions = [];


        stages.forEach(stage => {

            const node =
                stage.querySelector(".stage-node");


            if (!node) {
                return;
            }


            const rect =
                node.getBoundingClientRect();


            positions.push({

                x:
                    rect.left
                    -
                    journeyRect.left,

                y:
                    rect.top
                    -
                    journeyRect.top
                    +
                    rect.height / 2

            });

        });


        return positions;

    }



    /* ========================================================
       FIND SCROLL PROGRESS
    ======================================================== */

    function getProgress() {

        const rect =
            journey.getBoundingClientRect();


        const viewportHeight =
            window.innerHeight;


        const start =
            viewportHeight * 0.55;


        const end =
            rect.height
            -
            viewportHeight * 0.35;


        const current =
            -rect.top
            +
            start;


        return Math.max(
            0,
            Math.min(
                1,
                current / end
            )
        );

    }



    /* ========================================================
       INTERPOLATE
    ======================================================== */

    function interpolate(
        a,
        b,
        amount
    ) {

        return a +
            (b - a) *
            amount;

    }



    /* ========================================================
       CALCULATE ROBOT POSITION
    ======================================================== */

    function updateTarget() {

        const positions =
            getStagePositions();


        if (!positions.length) {
            return;
        }


        const progress =
            getProgress();


        const scaled =
            progress *
            (positions.length - 1);


        const index =
            Math.floor(scaled);


        const nextIndex =
            Math.min(
                index + 1,
                positions.length - 1
            );


        const localProgress =
            scaled - index;


        const first =
            positions[index];

        const second =
            positions[nextIndex];


        targetX =
            interpolate(
                first.x,
                second.x,
                localProgress
            );


        targetY =
            interpolate(
                first.y,
                second.y,
                localProgress
            );


        /*
         * Calculate direction of movement.
         */

        const dx =
            second.x -
            first.x;


        const dy =
            second.y -
            first.y;


        targetAngle =
            Math.atan2(
                dy,
                dx
            )
            *
            180
            /
            Math.PI;


        /*
         * Current active month
         */

        const newActiveStage =
            Math.min(
                Math.round(scaled),
                stages.length - 1
            );


        if (
            newActiveStage !==
            activeStage
        ) {

            activeStage =
                newActiveStage;


            stages.forEach(
                (stage, i) => {

                    stage.classList.toggle(
                        "active",
                        i === activeStage
                    );

                }
            );


            updateJourneyStatus(
                activeStage
            );

        }


        if (!ticking) {

            ticking = true;

            requestAnimationFrame(
                animateRobot
            );

        }

    }



    /* ========================================================
       ROBOT ANIMATION
    ======================================================== */

    function animateRobot() {

        const ease =
            0.075;


        currentX +=
            (targetX - currentX)
            *
            ease;


        currentY +=
            (targetY - currentY)
            *
            ease;


        currentAngle +=
            (targetAngle - currentAngle)
            *
            ease;


        robot.style.left =
            `${currentX}px`;


        robot.style.top =
            `${currentY}px`;


        /*
         * We don't rotate the whole robot strongly.
         * Only create a subtle direction tilt.
         */

        const tilt =
            Math.max(
                -10,
                Math.min(
                    10,
                    currentAngle - 90
                )
            );


        robot.style.transform =
            `translate(-50%, -50%)
             rotate(${tilt}deg)`;


        robot.classList.add(
            "active"
        );


        ticking = false;


        if (
            Math.abs(
                targetX - currentX
            ) > .5
            ||
            Math.abs(
                targetY - currentY
            ) > .5
        ) {

            requestAnimationFrame(
                animateRobot
            );

        }

    }



    /* ========================================================
       STATUS
    ======================================================== */

    function updateJourneyStatus(
        index
    ) {

        const status =
            document.getElementById(
                "journeyStatus"
            );


        if (!status) {
            return;
        }


        const stage =
            stages[index];


        if (!stage) {
            return;
        }


        const month =
            stage.dataset.month;


        status.textContent =
            `${month} checkpoint`;
    }



    /* ========================================================
       SCROLL
    ======================================================== */

    function handleScroll() {

        updateTarget();

    }


    window.addEventListener(
        "scroll",
        handleScroll,
        {
            passive: true
        }
    );


    window.addEventListener(
        "resize",
        updateTarget
    );


    /*
     * Initial position.
     */

    setTimeout(
        updateTarget,
        100
    );


});