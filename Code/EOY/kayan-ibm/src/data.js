export { 
  badgesAll, 
  badgesAgile, 
  badgesEDT, 
  badgesGarage, 
  badgesOther,
  rolesGraph,
  meterData
}

const badgesAll= [
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/a972f054-be07-4845-85c7-95c8d11852f5/IBM-Agile-Explorer.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/00cfeff7-03d2-4c00-b129-d2c09ca39831/IBM-Agile-Advocate.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/fb718a87-6d0d-4a6d-8068-677f1bec78f2/IBM_Garage_Essentials.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/9beccf39-df2f-4025-b971-3a7ec6dfdbfa/image.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/42aa8f4c-7b12-4d71-9fd9-246b96ef37ff/IBM_Garage_Practitioner.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/bc08972c-3c7d-4b99-82a0-c94bcca36674/Badges_v8-07_Practitioner.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/2700b813-82b8-4232-9b36-5dcd5cd24584/Badges_v8-08_Co-Creator.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/18cfda79-63fc-4a6d-a96c-2ffc9887cd3c/IBM-Quantum-Conversations.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/f4f08b45-aa38-4242-8b05-dcdac6811504/Deep_Learning_Essentials.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/3f393dd4-e8e0-4fef-a424-c9f1d1f3ba97/Open_Source_Foundations.png'
    },
  ];
  
  const badgesAgile = [
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/a972f054-be07-4845-85c7-95c8d11852f5/IBM-Agile-Explorer.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/00cfeff7-03d2-4c00-b129-d2c09ca39831/IBM-Agile-Advocate.png'
    },
  ];
  
  const badgesGarage = [
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/fb718a87-6d0d-4a6d-8068-677f1bec78f2/IBM_Garage_Essentials.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/9beccf39-df2f-4025-b971-3a7ec6dfdbfa/image.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/42aa8f4c-7b12-4d71-9fd9-246b96ef37ff/IBM_Garage_Practitioner.png'
    },
    // ... add more sections as needed
  ];
  
  const badgesEDT = [
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/bc08972c-3c7d-4b99-82a0-c94bcca36674/Badges_v8-07_Practitioner.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/2700b813-82b8-4232-9b36-5dcd5cd24584/Badges_v8-08_Co-Creator.png'
    },
  ];
  const badgesOther = [
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/18cfda79-63fc-4a6d-a96c-2ffc9887cd3c/IBM-Quantum-Conversations.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/f4f08b45-aa38-4242-8b05-dcdac6811504/Deep_Learning_Essentials.png'
    },
    {
      bgColor: "#ffffff",
      title: '',
      imgSrc: 'https://images.credly.com/size/680x680/images/3f393dd4-e8e0-4fef-a424-c9f1d1f3ba97/Open_Source_Foundations.png'
    },
    // ... add more sections as needed
  ];

const rolesGraph = {
  dummyData: [
    {
      "group": "OGV Process Automation",
      'groupMapsTo': 'hello4',
      'date':
        '2022-10-10',
      "value": [
        "20",
        '22'
      ],
    },
    {
      "group": "OGV Assistant",
      'groupMapsTo': 'hello4',
      'date':
        '2022-10-10',
      "value": [
        "20",
        '22'
      ],
    },
    {
      "group": "Destiny Squad Lead",
      'groupMapsTo': 'EXO',
      'date': '2022-09-01',
      'value': [
        "40",
        '50'
      ],
    },
    {
      "group": "Caibre Garage Lead",
      'date': '2022-10-01',
      'value': [
        "21",
        '24'
      ],
    },
    {
      "group": "Caibre Operations",
      'date': '2022-10-01',
      'value': [
        "21",
        '24'
      ],
    },
    {
      "group": "EXO Squad Lead",
      'date': '2022-10-01',
      'value': [
        "21",
        '24'
      ],
    },
    {
      "group": "EXO SM + PO ",
      'date': '2022-10-01',
      'value': [
        "21",
        '24'
      ],
    },
    
  ],
  options: {
    "title": "My Roles",
    'theme': 'g90',
    'animations': true,
    'color': { 
      'Dataset1': 'red',
    },
    // 'color': {
    //   'pairing':{
    //     'EXO': '8a3ffc',
    //   }
    // },
    "axes": {
      //'domain': [0,50],
      'limitDomainToBins': true,
      "left": {
        "mapsTo": "group",
        //'scaleType': 'time'
        "scaleType": "labels",
      },
      "bottom": {
        "mapsTo": "value",
        //'scaleType': 'time',
      },
    },
    "height": "400px",
    //'barPadding': '50px'
    //'barHeight':'100px',
  },
};

const meterData = { 
  
  someData: [
    [{
		  "group": "YL Hours",
		  "value": 300
	  }],
    [{
		  "group": "Events",
		  "value": 10
	  }],
    [{
		  "group": "Badges",
		  "value": 100
	  }],
  ],
options: {
	"meter": {
		"peak": 50
	},
	"height": '100px',
  'theme': 'g90',
},
}