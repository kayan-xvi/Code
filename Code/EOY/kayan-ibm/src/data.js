import DTLA from "./images/DTLA.png"

export {
  badgesAll,
  rolesGraph,
  meterData,
  lineChartOptions,
  pieData,
  pieOptions,
  radarData,
  radarOptions,
  lollyDataBig,
  lollyOptionsBig,
  lollyDataSmall,
  lollyOptionsSmall,
  badgeTags,
};

const badgeTags = [
  {
    title: "Select All",
  },
  {
    title: "Agile",
  },
  {
    title: "Garage",
  },
  {
    title: "Design",
  },
  {
    title: "Technology",
  },
  {
    title: "Other",
  },
  {
    title: "Coming Soon",
  },
];


const badgesAll = [
  {
    tags: "Agile",
    title: "My first badge on my third day",
    imgSrc:
      "https://images.credly.com/size/680x680/images/a972f054-be07-4845-85c7-95c8d11852f5/IBM-Agile-Explorer.png",
  },
  {
    tags: "Agile",
    title: "This badge marked my 6 months at IBM",
    imgSrc:
      "https://images.credly.com/size/680x680/images/00cfeff7-03d2-4c00-b129-d2c09ca39831/IBM-Agile-Advocate.png",
  },
  {
    tags: "Garage",
    title: "My first introduction to Garage",
    imgSrc:
      "https://images.credly.com/size/680x680/images/fb718a87-6d0d-4a6d-8068-677f1bec78f2/IBM_Garage_Essentials.png",
  },
  {
    tags: "Garage",
    title: "Another Garage badge",
    imgSrc:
      "https://images.credly.com/size/680x680/images/9beccf39-df2f-4025-b971-3a7ec6dfdbfa/image.png",
  },
  {
    tags: "Garage",
    title: "I only did this to get the Squad Lead badge",
    imgSrc:
      "https://images.credly.com/size/680x680/images/42aa8f4c-7b12-4d71-9fd9-246b96ef37ff/IBM_Garage_Practitioner.png",
  },
  {
    tags: "Garage",
    title: "This is the badge I am proudest of",
    imgSrc:
      "https://images.credly.com/size/680x680/images/12d0c938-bcbb-43c3-817e-f99e08362284/IBM_Garage_Squad_Leader.png",
  },
  {
    tags: "Design",
    title:
      "A nice refresher from product design, the only thing I've used from school",
    imgSrc:
      "https://images.credly.com/size/680x680/images/bc08972c-3c7d-4b99-82a0-c94bcca36674/Badges_v8-07_Practitioner.png",
  },
  {
    tags: "Design",
    title: "I completed this with Isabella, Jia and Tom",
    imgSrc:
      "https://images.credly.com/size/680x680/images/2700b813-82b8-4232-9b36-5dcd5cd24584/Badges_v8-08_Co-Creator.png",
  },
  {
    tags: "Design",
    title: "An in-depth dive on UI/UX",
    imgSrc:
      "https://udemy-certificate.s3.amazonaws.com/image/UC-326935e9-3cf4-4e8c-b1fd-94445daa8679.jpg?v=1689091816000",
  },
  {
    tags: "Technology",
    title: "A basic grasp on quantum",
    imgSrc:
      "https://images.credly.com/size/680x680/images/18cfda79-63fc-4a6d-a96c-2ffc9887cd3c/IBM-Quantum-Conversations.png",
  },
  {
    tags: "Technology",
    title: "Some technical insight on ML ",
    imgSrc:
      "https://images.credly.com/size/680x680/images/f4f08b45-aa38-4242-8b05-dcdac6811504/Deep_Learning_Essentials.png",
  },
  {
    tags: "Technology",
    title:
      "Completed for a client project I didn't go on, but understanding GitHub is useful",
    imgSrc:
      "https://images.credly.com/size/680x680/images/3f393dd4-e8e0-4fef-a424-c9f1d1f3ba97/Open_Source_Foundations.png",
  },
  {
    tags: "Technology",
    title:
      "Badge to show my understanding of DevSecOps ",
    imgSrc:
      "https://images.credly.com/size/680x680/images/6fcae0c0-78b7-48c5-a414-5d21665b2250/DevSecOps-Essentials.png",
  },
  {
    tags: "Other",
    title:
      "Helping to organise FTC x TechXchange Hack Your Financial Future Hackathon",
    imgSrc:
      "https://images.credly.com/size/680x680/images/c941deee-482b-4d54-8553-6b2abd481888/image.png",
  },
  {
    tags: "Other",
    title:
      "Shortlisted for Young Digital Professional of the Year ",
    imgSrc:
      DTLA,
  },
  {
    tags: "Coming Soon",
    title:
      "Woo I'm going to be a Registered Scrum Master",
    imgSrc:
      "https://agileeducation.org/wp-content/uploads/2019/08/ScrumMaster-Badge.png",
  },
  {
    tags: "Coming Soon",
    title:
      "Dependent on getting RSM Certified",
    imgSrc:
      "https://images.credly.com/size/680x680/images/6fdeb718-400f-4336-8dea-ae10feb8ce3d/image.png",
  },
  {
    tags: "Coming Soon",
    title:
      "If I can claim it for the learning I've done",
    imgSrc:
      "https://images.credly.com/size/680x680/images/ab8db642-5d52-445a-9c63-2237c2160df1/image.png",
  },
  {
    tags: "Coming Soon",
    title:
      "These badges really are just markers - will show 12 months at IBM",
    imgSrc:
      "https://images.credly.com/size/680x680/images/6de79642-54f4-42d5-8ec6-4e02aec75ae2/IBM-Agile-Achiever.png",
  },
  {
    tags: "Coming Soon",
    title:
      "A basic grasp on Cloud while I'm here",
    imgSrc:
      "https://images.credly.com/size/680x680/images/b0607951-b6f7-47d0-af16-7112971ab2ef/Cloud_Core_-_Developer_Skills_Network_-_v3.png",
  },
  {
    tags: "Coming Soon",
    title:
      "A basic grasp on Blockchain while I'm here",
    imgSrc:
      "https://images.credly.com/size/680x680/images/0b831161-bca5-4118-97c5-df106a5f6515/IBM-Blockchain-Foundation-Consulting.png",
  },
  {
    tags: "Coming Soon",
    title:
      "Dependent on SM Intermediate and to show the learning I've done",
    imgSrc:
      "https://images.credly.com/size/680x680/images/fd9537fb-5065-4f37-986d-18769cf8f4f4/image.png",
  },
];

const lineChartOptions = {
  title: "Roles",
  axes: {
    bottom: {
      mapsTo: "date",
      scaleType: "time",
    },
    left: {
      mapsTo: "groupMapsTo",
      scaleType: "labels",
    },
  },
  height: "800px",
  curve: "curveMonotoneX",
  theme: "g90",
  legend: {
    order: ["EXOPOC", "Caibre", "Destiny", "OGV", "Misc", "Giveback"],
  },
  animations: true,
};

const rolesGraph = [
  {
    group: "Giveback",
    groupMapsTo: "FTC Hackathon",
    date: "2023-06-15",
  },
  {
    group: "Giveback",
    groupMapsTo: "FTC Hackathon",
    date: "2022-11-17",
  },
  {
    group: "Giveback",
    groupMapsTo: "FIC Committee",
    date: "2023-03-08",
  },
  {
    group: "Giveback",
    groupMapsTo: "FIC Committee",
    date: "2022-10-21",
  },
  {
    group: "Giveback",
    groupMapsTo: "BTZ Rebranding",
    date: "2022-11-23",
  },
  {
    group: "Giveback",
    groupMapsTo: "BTZ Rebranding",
    date: "2022-10-13",
  },
  {
    group: "Misc",
    groupMapsTo: "watsonx challenge",
    date: "2023-08-12",
  },
  {
    group: "Misc",
    groupMapsTo: "watsonx challenge",
    date: "2023-08-04",
  },
  {
    group: "Misc",
    groupMapsTo: "iX FS Strategy",
    date: "2023-07-19",
  },
  {
    group: "Misc",
    groupMapsTo: "iX FS Strategy",
    date: "2023-06-23",
  },
  {
    group: "OGV",
    groupMapsTo: "KIOps",
    date: "2023-08-01",
  },
  {
    group: "OGV",
    groupMapsTo: "KIOps",
    date: "2023-05-15",
  },
  {
    group: "OGV",
    groupMapsTo: "VA Assistant",
    date: "2023-05-15",
  },
  {
    group: "OGV",
    groupMapsTo: "VA Assistant",
    date: "2023-04-04",
  },
  {
    group: "Caibre",
    groupMapsTo: "Garage Lead",
    date: "2023-03-20",
  },
  {
    group: "Caibre",
    groupMapsTo: "Garage Lead",
    date: "2023-03-01",
  },
  {
    group: "Caibre",
    groupMapsTo: "Operations",
    date: "2022-12-20",
  },
  {
    group: "Caibre",
    groupMapsTo: "Operations",
    date: "2023-03-31",
  },
  {
    group: "Destiny",
    groupMapsTo: "Squad Lead",
    date: "2023-08-01",
  },
  {
    group: "Destiny",
    groupMapsTo: "Squad Lead",
    date: "2023-03-10",
  },
  {
    group: "Caibre",
    groupMapsTo: "Squad Lead",
    date: "2023-03-10",
  },
  {
    group: "Caibre",
    groupMapsTo: "Squad Lead",
    date: "2023-01-16",
  },
  {
    group: "EXOPOC",
    groupMapsTo: "Squad Lead",
    date: "2023-01-16",
  },
  {
    group: "EXOPOC",
    groupMapsTo: "Squad Lead",
    date: "2022-12-01",
  },
  {
    group: "EXOPOC",
    groupMapsTo: "SM + PO",
    date: "2022-11-31",
  },
  {
    group: "EXOPOC",
    groupMapsTo: "SM + PO",
    date: "2022-09-12",
  },
];

const meterData = {
  someData: [
    [
      {
        group: "Both Travellators Working in Waterloo Station",
        value: 8,
      },
    ],
    [
      {
        group: "Value Generated ",
        value: 310,
      },
    ],
  ],
  options: {
    meter: {
    },
    height: "100px",
    theme: "g90",
  },
};

const pieData = [
  {
    group: "Completed",
    value: 10,
  },
  {
    group: "In Progress",
    value: 4,
  },
  {
    group: "Rejected",
    value: 1,
  },
];

const pieOptions = {
  title: "Goals",
  resizable: true,
  height: "350px",
  width: "300px",
  gauge: {
    type: "full",
  },
  color: {
    scale: {
      value: "#FFFFFF",
    },
  },
  theme: "g90",
};

const radarData = [
  {
    product: "Before",
    feature: "Confidence",
    score: 45,
  },
  {
    product: "Before",
    feature: "Technical Knowledge",
    score: 7,
  },
  {
    product: "Before",
    feature: "Delivery Knowledge",
    score: 5,
  },
  {
    product: "Before",
    feature: "Beard",
    score: 63,
  },
  {
    product: "Before",
    feature: "Bench Press",
    score: 47,
  },
  {
    product: "Before",
    feature: "People Management",
    score: 15,
  },
  {
    product: "Before",
    feature: "Design Knowlede",
    score: 13,
  },
  {
    product: "After",
    feature: "Confidence",
    score: 93,
  },
  {
    product: "After",
    feature: "Technical Knowledge",
    score: 37,
  },
  {
    product: "After",
    feature: "Delivery Knowledge",
    score: 87,
  },
  {
    product: "After",
    feature: "Beard",
    score: 83,
  },
  {
    product: "After",
    feature: "Bench Press",
    score: 64.5,
  },
  {
    product: "After",
    feature: "People Management",
    score: 75,
  },
  {
    product: "After",
    feature: "Design Knowlede",
    score: 63,
  },
];

const radarOptions = {
  title: "Personal Development",
  radar: {
    axes: {
      angle: "feature",
      value: "score",
    },
  },
  data: {
    groupMapsTo: "product",
  },
  height: "400px",
  width: "500px",
  theme: "g90",
};

const lollyDataBig = [
  {
    group: "Role",
    key: "Tickets Created",
    value: 237,
  },
  {
    group: "Role",
    key: "Meetings",
    value: 44 + 61 + 57 + 77 + 66 + 93 + 103 + 84 + 78 + 78 + 71,
    // Sept 44
    // Oct 61
    // Nov 57
    // Dec 77
    // Jan 66
    // Feb 93
    // Mar 103
    // Apr 84
    // May 78
    // Jun 78
    // Jul 71
  },
  {
    group: "Personal Development", 
    key: "YL Hours",
    value: 227,
  },
  {
    group: "Other",
    key: "Slides Made",
    value: 111,
  },
  {
    group: "Other",
    key: "Lines of Code",
    value: 588 + 153 + 165 + 76 + 17,
    // Data.js 588
    // App.js 153 
    // App.scss 156
    // Index.js 76
    // Index.scss 17
  },
];

const lollyOptionsBig = {
  theme: "g90",
  axes: {
    bottom: {
      scaleType: "labels",
      mapsTo: "key",
    },
    left: {
      mapsTo: "value",
    },
  },
  height: "350px",
  width: "700px",
};

const lollyDataSmall = [
  {
    group: "Work",
    key: "THINK Projects",
    value: 2,
  },
  {
    group: "Work",
    key: "POCs/ Iterations Delivered",
    value: 13,
  },
  {
    group: "Work",
    key: "People Managed",
    value: 36,
  },
  {
    group: "Personal Development",
    key: "Badges",
    value: 12,
  },
  {
    group: "Personal Development",
    key: "Feecback Received",
    value: 24, // as of 5 jul
  },
  {
    group: "Other",
    key: "Books Read",
    value: 25,
  },
  {
    group: "Other",
    key: "IBM T-Shirts",
    value: 3,
  },
];

const lollyOptionsSmall = {
  theme: "g90",
  axes: {
    bottom: {
      scaleType: "labels",
      mapsTo: "key",
    },
    left: {
      mapsTo: "value",
    },
  },
  height: "400px",
  width: "700px",
};