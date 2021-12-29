"""
motivation for this config being in python: json is easy to screw up

we'll maintain settings in dicts here and then generate json and markdown outputs
"""
import copy
import pandas as pd
import os


dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

TOKENS = {
  ##################
  # 1. Solana native
  ##################
  "ATLAS": {
    "symbol": "ATLAS",
    "name": "Star Atlas (Wormhole)",
    "destAddresses": {
      "eth": "0xb9F747162AB1E95d07361f9048BcDF6eDdA9eEA7",
      "terra": "terra1rg8f993m9834afwazersesgx7jjxv4p87q9wvc",
      "bsc": "0x83850D97018f665EB746FBb8f18351e977d1b0D6",
    },
    "origin": "sol",
    "sourceAddress": "ATLASXmbPQxBUYbxPsV97usA3fPQYEqzQBUHgiFCUsXx",
    "coingeckoId": "star-atlas",
  },
  "AURY": {
    "symbol": "AURY",
    "name": "Aurory (Wormhole)",
    "destAddresses": {
      "bsc": "0xF5a367b7809e5683538C93Ce638B9258A0B88271",
    },
    "origin": "sol",
    "sourceAddress": "AURYydfxJib1ZkTir1Jn1J9ECYUtjb6rKQVmtYaixWPP",
    "coingeckoId": "aurory",
  },
  "RAY": {
    "symbol": "RAY",
    "name": "Raydium (Wormhole)",
    "destAddresses": {
      "eth": "0xE617dd80c621a5072bD8cBa65E9d76c07327004d",
      "terra": "terra1ht5sepn28z999jx33sdduuxm9acthad507jg9q",
      "bsc": "0x13b6A55662f6591f8B8408Af1C73B017E32eEdB8",
    },
    "origin": "sol",
    "sourceAddress": "4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R",
    "coingeckoId": "raydium",
  },
  "SBR": {
    "symbol": "SBR",
    "name": "Saber (Wormhole)",
    "destAddresses": {
      "terra": "terra17h82zsq6q8x5tsgm5ugcx4gytw3axguvzt4pkc",
      "bsc": "0x75344E5693ed5ecAdF4f292fFeb866c2cF8afCF1",
    },
    "origin": "sol",
    "sourceAddress": "0x75344E5693ed5ecAdF4f292fFeb866c2cF8afCF1",
    "coingeckoId": "saber",
  },
  "SOL": {
    "symbol": "SOL",  # technically wrapped SOL
    "name": "SOL (Wormhole)",
    "destAddresses": {
      "eth": "0xD31a59c85aE9D8edEFeC411D448f90841571b89c",
      "terra": "terra190tqwgqx7s8qrknz6kckct7v607cu068gfujpk",
      "bsc": "0xfA54fF1a158B5189Ebba6ae130CEd6bbd3aEA76e",
      "avax": "0xFE6B19286885a4F7F55AdAD09C3Cd1f906D2478F",
    },
    "origin": "sol",
    "sourceAddress": "So11111111111111111111111111111111111111112",
    "coingeckoId": "solana",
  },
  "SRMso": {
    "symbol": "SRMso",
    "name": "Serum (Wormhole from Solana)",
    "destAddresses": {
      "eth": "0xE3ADAA4fb7c92AB833Ee08B3561D9c434aA2A3eE",
      "terra": "terra1dkam9wd5yvaswv4yq3n2aqd4wm5j8n82qc0c7c",
      "bsc": "0x12BeffdCEcb547640DC30e1495E4B9cdc21922b4",
    },
    "origin": "sol",
    "sourceAddress": "SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt",
    "coingeckoId": "serum",
  },
  "USDCso": {
    "symbol": "USDCso",
    "name": "USD Coin (Wormhole from Solana)",
    "destAddresses": {
      "eth": "0x41f7B8b9b897276b7AAE926a9016935280b44E97",
      "terra": "terra1e6mq63y64zcxz8xyu5van4tgkhemj3r86yvgu4",
      "bsc": "0x91Ca579B0D47E5cfD5D0862c21D5659d39C8eCf0",
      "avax": "0x0950Fc1AD509358dAeaD5eB8020a3c7d8b43b9DA",
    },
    "origin": "sol",
    "sourceAddress": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
    "coingeckoId": "usd-coin",
  },
  "USDTso": {
    "symbol": "USDTso",
    "name": "Tether USD (Wormhole from Solana)",
    "destAddresses": {
      "eth": "0x1CDD2EaB61112697626F7b4bB0e23Da4FeBF7B7C",
      "terra": "terra1hd9n65snaluvf7en0p4hqzse9eqecejz2k8rl5",
      "bsc": "0x49d5cC521F75e13fa8eb4E89E9D381352C897c96",
      "avax": "0xF0FF231e3F1A50F83136717f287ADAB862f89431",
    },
    "origin": "sol",
    "sourceAddress": "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB",
    "coingeckoId": "tether",
  },
  "mSOL": {
    "symbol": "mSOL",
    "name": "Marinade staked SOL (Wormhole)",
    "destAddresses": {
      "eth": "0x756bFb452cFE36A5Bc82e4F5f4261A89a18c242b",
      "terra": "terra1qvlpf2v0zmru3gtex40sqq02wxp39x3cjh359y",
    },
    "origin": "sol",
    "sourceAddress": "mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So",
    "coingeckoId": "marinade-staked-sol",
  },

  #####################
  # 2. Ethereum native
  #####################
  "1SOL": {
    "symbol": "1SOL",
    "name": "1sol.io (Wormhole)",
    "destAddresses": {
      "sol": "4ThReWAbAVZjNVgs5Ui9Pk3cZ5TYaD9u6Y89fp6EFzoF",
    },
    "origin": "eth",
    "sourceAddress": "0x009178997aff09a67d4caccfeb897fb79d036214",
    "coingeckoId": "1sol",
  },
  "AXSet": {
    "symbol": "AXSet",
    "name": "Axie Infinity Shard (Wormhole from Ethereum)",
    "destAddresses": {
      "sol": "HysWcbHiYY9888pHbaqhwLYZQeZrcQMXKQWRqS7zcPK5",
      "bsc": "0x556b60c53fbC1518Ad17E03d52E47368dD4d81B3",
    },
    "origin": "eth",
    "sourceAddress": "0xbb0e17ef65f82ab018d8edd776e8dd940327b28b",
    "coingeckoId": "axie-infinity",
  },
  "BUSDet": {
    "symbol": "BUSDet",
    "name": "Binance USD (Wormhole from Ethereum)",
    "destAddresses": {
      "sol": "33fsBLA8djQm82RpHmE3SuVrPGtZBWNYExsEUeKX1HXX",
      "bsc": "0x035de3679E692C471072d1A09bEb9298fBB2BD31",
    },
    "origin": "eth",
    "sourceAddress": "0x4fabb145d64652a948d72533023f6e7a623c7c53",
    "coingeckoId": "binance-usd",
  },
  "DAI": {
    "symbol": "DAI",
    "name": "DAI (Wormhole)",
    "destAddresses": {
      "sol": "EjmyN6qEC1Tf1JxiG1ae7UTJhUxSwk1TCWNWqxWV4J6o",
      "bsc": "0x3413a030EF81a3dD5a302F4B4D11d911e12ed337",
      "terra": "terra1zmclyfepfmqvfqflu8r3lv6f75trmg05z7xq95",
    },
    "origin": "eth",
    "sourceAddress": "0x6b175474e89094c44da98b954eedeac495271d0f",
    "coingeckoId": "dai",
  },
  "DYDX": {
    "symbol": "DYDX",
    "name": "dYdX (Wormhole)",
    "destAddresses": {
      "sol": "4Hx6Bj56eGyw8EJrrheM6LBQAvVYRikYCWsALeTrwyRU",
    },
    "origin": "eth",
    "sourceAddress": "0x92d6c1e31e14520e676a687f0a93788b716beff5",
    "coingeckoId": "dydx",
  },
  "ETH": {  # WETH
    "symbol": "ETH",
    "name": "Ether (Wormhole)",
    "destAddresses": {
      "sol": "7vfCXTUXx5WJV5JADk17DUJ4ksgau7utNKj4b963voxs",
      "bsc": "0x4DB5a66E937A9F4473fA95b1cAF1d1E1D62E29EA",
      "terra": "terra14tl83xcwqjy0ken9peu4pjjuu755lrry2uy25r",
      "matic": "0x11CD37bb86F65419713f30673A480EA33c826872",
      "avax": "0x8b82A291F83ca07Af22120ABa21632088fC92931",
    },
    "origin": "eth",
    "sourceAddress": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
    "coingeckoId": "ether",
  },
  "FRAX": {
    "symbol": "FRAX",
    "name": "Frax (Wormhole)",
    "destAddresses": {
      "sol": "FR87nWEUxVgerFGhZM8Y4AggKGLnaXswr1Pd8wZ4kZcp",
    },
    "origin": "eth",
    "sourceAddress": "0x853d955acef822db058eb8505911ed77f175b99e",
    "coingeckoId": "frax",
  },
  "FTT": {
    "symbol": "FTT",
    "name": "FTX Token (Wormhole)",
    "destAddresses": {
      "sol": "EzfgjvkSwthhgHaceR3LnKXUoRkP6NUhfghdaHAj1tUv",
      "bsc": "0x49BA054B9664e99ac335667a917c63bB94332E84",
    },
    "origin": "eth",
    "sourceAddress": "0x50d1c9771902476076ecfc8b2a83ad6b9355a4c9",
    "coingeckoId": "ftx-token",
  },
  "FXS": {
    "symbol": "FXS",
    "name": "Frax Share (Wormhole)",
    "destAddresses": {
      "sol": "6LX8BhMQ4Sy2otmAWj7Y5sKd9YTVVUgfMsBzT6B9W7ct",
    },
    "origin": "eth",
    "sourceAddress": "0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0",
    "coingeckoId": "frax-share",
  },
  "LDO": {
    "symbol": "LDO",
    "name": "Lido DAO (Wormhole)",
    "destAddresses": {
      "bsc": "0x986854779804799C1d68867F5E03e601E781e41b",
      "sol": "HZRCwxP2Vq9PCpPXooayhJ2bxTpo5xfpQrwB1svh332p",
      "terra": "terra1jxypgnfa07j6w92wazzyskhreq2ey2a5crgt6z",
    },
    "origin": "eth",
    "sourceAddress": "0x5a98fcbea516cf06857215779fd812ca3bef1b32",
    "coingeckoId": "lido-dao",
  },
  "LINK": {
    "symbol": "LINK",
    "name": "Chainlink (Wormhole)",
    "destAddresses": {
      "sol": "2wpTofQ8SkACrkZWrZDjXPitYa8AwWgX8AfxdeBRRVLX",
      "terra": "terra12dfv3f0e6m22z6cnhfn3nxk2en3z3zeqy6ctym",
    },
    "origin": "eth",
    "sourceAddress": "0x514910771af9ca656af840dff83e8264ecf986ca",
    "coingeckoId": "chainlink",
  },
  "MIMet": {
    "symbol": "MIMet",
    "name": "Magic Internet Money (Wormhole from Ethereum)",
    "destAddresses": {
      "sol": "HRQke5DKdDo3jV7wnomyiM8AA3EzkVnxMDdo2FQ5XUe1",
      "terra": "terra15a9dr3a2a2lj5fclrw35xxg9yuxg0d908wpf2y",
    },
    "origin": "eth",
    "sourceAddress": "0x99d8a9c45b2eca8864373a26d1459e3dff1e17f3",
    "coingeckoId": "magic-internet-money",
  },
  "SHIB": {
    "symbol": "SHIB",
    "name": "Shiba Inu (Wormhole)",
    "destAddresses": {
      "sol": "CiKu4eHsVrc1eueVQeHn7qhXTcVu95gSQmBpX4utjL9z",
      "bsc": "0xb1547683DA678f2e1F003A780143EC10Af8a832B",
      "terra": "terra1huku2lecfjhq9d00k5a8dh73gw7dwe6vvuf2dd",
    },
    "origin": "eth",
    "sourceAddress": "0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce",
    "coingeckoId": "shiba-inu",
  },
  "SRMet": {
    "symbol": "SRMet",
    "name": "Serum (Wormhole from Ethereum)",
    "destAddresses": {
      "sol": "xnorPhAzWXUczCP3KjU5yDxmKKZi5cSbxytQ1LgE3kG",
      "bsc": "0xd63CDf02853D759831550fAe7dF8FFfE0B317b39",
    },
    "origin": "eth",
    "sourceAddress": "0x476c5e26a75bd202a9683ffd34359c0cc15be0ff",
    "coingeckoId": "serum",
  },
  "SUSHI": {
    "symbol": "SUSHI",
    "name": "SushiToken (Wormhole)",
    "destAddresses": {
      "sol": "ChVzxWRmrTeSgwd3Ui3UumcN8KX7VK3WaD4KGeSKpypj",
      "bsc": "0x3524fd7488fdb1F4723BBc22C9cbD1Bf89f46E3B",
      "terra": "terra1csvuzlf92nyemu6tv25h0l79etpe8hz3h5vn4a",
    },
    "origin": "eth",
    "sourceAddress": "0x6b3595068778dd592e39a122f4f5a5cf09c90fe2",
    "coingeckoId": "sushi",
  },
  "UNI": {
    "symbol": "UNI",
    "name": "Uniswap (Wormhole)",
    "destAddresses": {
      "sol": "8FU95xFJhUUkyyCLU13HSzDLs7oC4QZdXQHL6SCeab36",
      "terra": "terra1wyxkuy5jq545fn7xfn3enpvs5zg9f9dghf6gxf",
    },
    "origin": "eth",
    "sourceAddress": "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984",
    "coingeckoId": "uniswap",
  },
  "USDCet": {
    "symbol": "USDCet",
    "name": "USD Coin (Wormhole from Ethereum)",
    "destAddresses": {
      "sol": "A9mUU4qviSctJVPJdBJWkb28deg915LYJKrzQ19ji3FM",
      "terra": "terra1pepwcav40nvj3kh60qqgrk8k07ydmc00xyat06",
      "bsc": "0xB04906e95AB5D797aDA81508115611fee694c2b3",
      "avax": "0xB24CA28D4e2742907115fECda335b40dbda07a4C",
      "matic": "0x4318CB63A2b8edf2De971E2F17F77097e499459D", 
    },
    "origin": "eth",
    "sourceAddress": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "coingeckoId": "usd-coin",
  },
  "USDK": {
    "symbol": "USDK",
    "name": "USDK (Wormhole)",
    "destAddresses": {
      "sol": "43m2ewFV5nDepieFjT9EmAQnc1HRtAF247RBpLGFem5F",
    },
    "origin": "eth",
    "sourceAddress": "0x1c48f86ae57291f7686349f12601910bd8d470bb",
    "coingeckoId": "usdk",
  },
  "USDTet": {
    "symbol": "USDTet",
    "name": "Tether USD (Wormhole from Ethereum)",
    "destAddresses": {
      "sol": "Dn4noZ5jgGfkntzcQSUZ8czkreiZ1ForXYoV2H8Dm7S1",
      "terra": "terra1ce06wkrdm4vl6t0hvc0g86rsy27pu8yadg3dva",
      "bsc": "0x524bC91Dc82d6b90EF29F76A3ECAaBAffFD490Bc",
      "matic": "0x9417669fBF23357D2774e9D421307bd5eA1006d2",
    },
    "origin": "eth",
    "sourceAddress": "0xdac17f958d2ee523a2206206994597c13d831ec7",
    "coingeckoId": "tether",
  },
  "WBTC": {
    "symbol": "WBTC",
    "name": "Wrapped BTC (Wormhole)",
    "destAddresses": {
      "sol": "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh",
      "terra": "terra1aa7upykmmqqc63l924l5qfap8mrmx5rfdm0v55",
      "matic": "0x5D49c278340655B56609FdF8976eb0612aF3a0C3",
    },
    "origin": "eth",
    "sourceAddress": "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
    "coingeckoId": "wrapped-bitcoin",
  },
  "gOHM": {
    "symbol": "gOHM",
    "name": "Governance OHM (Wormhole)",
    "destAddresses": {
      "sol": "FUGsN8H74WjRBBMfQWcf9Kk32gebA9VnNaGxqwcVvUW7",
      "terra": "terra1fpfn2kkr8mv390wx4dtpfk3vkjx9ch3thvykl3",
    },
    "origin": "eth",
    "sourceAddress": "0x0ab87046fbb341d058f17cbc4c1133f25a20a52f",
    "coingeckoId": "governance-ohm",
  },
  "ibBTC": {
    "symbol": "ibBTC",
    "name": "Interest Bearing Bitcoin (Wormhole)",
    "destAddresses": {
      "sol": "Bzq68gAVedKqQkQbsM28yQ4LYpc2VComDUD9wJBywdTi",
    },
    "origin": "eth",
    "sourceAddress": "0xc4e15973e6ff2a35cc804c2cf9d2a1b817a8b40f",
    "coingeckoId": "interest-bearing-bitcoin",
  },
  "stETH": {
    "symbol": "stETH",
    "name": "Lido Staked Ether (Wormhole)",
    "destAddresses": {
      "sol": "H2mf9QNdU2Niq6QR7367Ua2trBsvscLyX5bz7R3Pw5sE",
      "terra": "terra1w7ywr6waxtjuvn5svk5wqydqpjj0q9ps7qct4d",
    },
    "origin": "eth",
    "sourceAddress": "0xae7ab96520de3a18e5e111b5eaab095312d7fe84",
    "coingeckoId": "lido-staked-ether",
  },

  #################
  # 3. Terra native
  #################
  "UST": {
    "symbol": "UST",
    "name": "UST (Wormhole)",
    "destAddresses": {
      "eth": "0xa693b19d2931d498c5b318df961919bb4aee87a5",
      "bsc": "0x3d4350cD54aeF9f9b2C29435e0fa809957B3F30a",
      "matic": "0xE6469Ba6D2fD6130788E0eA9C0a0515900563b59",
      "avax": "0xb599c3590F42f8F995ECfa0f85D2980B76862fc1",
    },
    "origin": "terra",
    "sourceAddress": "uusd",
    "coingeckoId": "terra-usd",
  },
  "LUNA": {
    "symbol": "LUNA",
    "name": "LUNA (Wormhole)",
    "destAddresses": {
      "eth": "0xbd31ea8212119f94a611fa969881cba3ea06fa3d",
      "bsc": "0x156ab3346823B651294766e23e6Cf87254d68962",
      "matic": "0x9cd6746665D9557e1B9a775819625711d0693439",
      "avax": "0x70928E5B188def72817b7775F0BF6325968e563B",
    },
    "origin": "terra",
    "sourceAddress": "uluna",
    "coingeckoId": "terra-luna",
  },

  ###################
  # 4. BSC native
  ###################
  "BNB": {
    "symbol": "BNB",
    "name": "Binance Coin (Wormhole)",
    "destAddresses": {
      "sol": "9gP2kCy3wA1ctvYWQk75guqXuHfrEomqydHLtcTCqiLa",
      "eth": "0x418D75f65a02b3D53B2418FB8E1fe493759c7605",
      "terra": "terra1cetg5wruw2wsdjp7j46rj44xdel00z006e9yg8",
      "avax": "0x442F7f22b1EE2c842bEAFf52880d4573E9201158",
    },
    "origin": "bsc",
    "sourceAddress": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c",
    "coingeckoId": "binance-coin",
  },
  "BUSDbs": {
    "symbol": "BUSDbs",
    "name": "Binance USD (Wormhole from BSC)",
    "destAddresses": {
      "sol": "5RpUwQ8wtdPCZHhu6MERp2RGrpobsbZ6MH5dDHkUjs2",
      "eth": "0x7B4B0B9b024109D182dCF3831222fbdA81369423",
      "terra": "terra1skjr69exm6v8zellgjpaa2emhwutrk5a6dz7dd",
      "avax": "0xA41a6c7E25DdD361343e8Cb8cFa579bbE5eEdb7a",
    },
    "origin": "bsc",
    "sourceAddress": "0xe9e7cea3dedca5984780bafc599bd69add087d56",
    "coingeckoId": "binance-usd",
  },
  "CAKE": {
    "symbol": "CAKE",
    "name": "PancakeSwap Token (Wormhole)",
    "destAddresses": {
      "eth": "J8LKx7pr9Zxh9nMhhT7X3EBmj5RzuhFrHKyJAe2F2i9S",
      "terra": "terra1xvqlpjl2dxyel9qrp6qvtrg04xe3jh9cyxc6av",
      "avax": "0x98a4d09036Cc5337810096b1D004109686E56Afc",
    },
    "origin": "bsc",
    "sourceAddress": "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
    "coingeckoId": "pancakeswap",
  },
  "USDCbs": {
    "symbol": "USDCbs",
    "name": "USD Coin (Wormhole from BSC)",
    "destAddresses": {
      "sol": "FCqfQSujuPxy6V42UvafBhsysWtEq1vhjfMN1PUbgaxA",
      "eth": "0x7cd167B101D2808Cfd2C45d17b2E7EA9F46b74B6",
      "terra": "terra1yljlrxvkar0c6ujpvf8g57m5rpcwl7r032zyvu",
      "avax": "0x6145E8a910aE937913426BF32De2b26039728ACF",
    },
    "origin": "bsc",
    "sourceAddress": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
    "coingeckoId": "usd-coin",
  },
  "USDTbs": {
    "symbol": "USDTbs",
    "name": "Tether USD (Wormhole from BSC)",
    "destAddresses": {
      "sol": "8qJSyQprMC57TWKaYEmetUR3UUiTP2M3hXdcvFhkZdmv",
      "eth": "0xDe60aDfDdAAbaAAC3dAFa57B26AcC91Cb63728c4",
      "terra": "terra1vlqeghv5mt5udh96kt5zxlh2wkh8q4kewkr0dd",
      "avax": "0xA67BCC0D06d7d13A13A2AE30bF30f1B434f5a28B",
    },
    "origin": "bsc",
    "sourceAddress": "0x55d398326f99059fF775485246999027B3197955",
    "coingeckoId": "tether",
  },

  ###################
  # 5. Polygon native
  ###################
  "USDCpo": {
    "symbol": "USDCpo",  # double-bridged tether: ERC-20 -> Polygon (via PoS bridge)
    "name": "USD Coin (PoS) (Wormhole from Polygon)",
    "destAddresses": {
      "sol": "E2VmbootbVCBkMNNxKQgCLMS1X3NoGMaYAsufaAsf7M",
      "eth": "0x566957eF80F9fd5526CD2BEF8BE67035C0b81130",
      "terra": "terra1kkyyh7vganlpkj0gkc2rfmhy858ma4rtwywe3x",
      "bsc": "0x672147dD47674757C457eB155BAA382cc10705Dd",
      "avax": "0x543672E9CBEC728CBBa9C3Ccd99ed80aC3607FA8",
    },
    "origin": "matic",
    "sourceAddress": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
    "coingeckoId": "usd-coin",
  },
  "MATICpo": {
    # this is mega-confusing because there is
    # 1. ERC-20 MATIC (we call MATICet)
    # 2. MATIC (native token of polygon) (0x0000000000000000000000000000000000001010)
    # 3. wrapped MATIC (we call MATICpo)
    "symbol": "MATICpo",
    "name": "MATIC (Wormhole from Polygon)",
    "destAddresses": {
      "sol": "Gz7VkD4MacbEB6yC5XD3HcumEiYx2EtDYYrfikGsvopG",  # covered by token-list
      "eth": "0x7c9f4C87d911613Fe9ca58b579f737911AAD2D43",
      "terra": "terra1dtqlfecglk47yplfrtwjzyagkgcqqngd5lgjp8",
      "bsc": "0xc836d8dC361E44DbE64c4862D55BA041F88Ddd39",
      "avax": "0xf2f13f0B7008ab2FA4A2418F4ccC3684E49D20Eb",
    },
    "origin": "matic",
    "sourceAddress": "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270",
    "coingeckoId": "polygon",
  },

  #################
  # 6. AVAX native
  #################
  "AVAX": {
    "symbol": "AVAX",  # technically wrapped AVAX
    "name": "AVAX (Wormhole)",
    "destAddresses": {
      "sol": "KgV1GvrHQmRBY8sHQQeUKwTm2r2h8t4C8qt12Cw1HVE",  # covered by token-list
      "eth": "0x85f138bfEE4ef8e540890CFb48F620571d67Eda3",
      "terra": "terra1hj8de24c3yqvcsv9r8chr03fzwsak3hgd8gv3m",
      "bsc": "0x96412902aa9aFf61E13f085e70D3152C6ef2a817",
      "matic": "0x7Bb11E7f8b10E9e571E5d8Eace04735fDFB2358a",
    },
    "origin": "avax",
    "sourceAddress": "0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7",
    "coingeckoId": "avalanche",
  },
  "JOE": {
    "symbol": "JOE",
    "name": "JoeToken (Wormhole)",
    "destAddresses": {
      "sol": "CriXdFS9iRAYbGEQiTcUqbWwG9RBmYt5B6LwTnoJ61Sm",  # covered by token-list
    },
    "origin": "avax",
    "sourceAddress": "0x6e84a6216ea6dacc71ee8e6b0a5b7322eebc0fdd",
    "coingeckoId": "joe",
  },

  #################
  # 7. Oasis native
  #################
  # "": {
  #   "symbol": "",
  #   "name": " (Wormhole)",
  #   "destAddresses": {
  #     "eth": "",
  #     "bsc": "",
  #     "terra": "",
  #   },
  #   "origin": "",
  #   "sourceAddress": "",
  #   "coingeckoId": "",
  # },
}

SOURCE_INFO = {
  'eth': ('Ethereum', 'et', "https://etherscan.io", "https://etherscan.io/address/0x3ee18B2214AFF97000D974cf647E7C347E8fa585"),
  'bsc': ('BSC', 'bs', "https://bscscan.com", "https://bscscan.com/address/0xB6F6D86a8f9879A9c87f643768d9efc38c1Da6E7"),
  'terra': ('Terra', 'te', "https://finder.terra.money/columbus-5", "https://finder.terra.money/columbus-5/address/terra10nmmwe8r3g99a9newtqa7a75xfgs2e8z87r2sf"),
  'matic': ('Polygon', 'po', "https://polygonscan.com", "https://polygonscan.com/address/0x5a58505a96d1dbf8df91cb21b54419fc36e93fde"),
  'avax': ('Avalanche', 'av', "https://snowtrace.io", "https://snowtrace.io/address/0x0e082f06ff657d94310cb8ce8b0d9a04541d8052"),
  'sol': ('Solana', 'so', "https://solscan.io", "https://solscan.io/account/wormDTUJ6AWPNvk59vGQbDvGJmqbDTdgWgAqcLBCgUb"),
  # 'algo': ('Algorand', 'al'),
}


def _link_address(dest, addr):
  category = 'address' if dest == 'terra' else 'token'
  return "[%s](%s/%s/%s)" % (addr, SOURCE_INFO[dest][2], category, addr)


def _link_coingecko(name, coingecko_id):
  if pd.isna(coingecko_id):
    return name
  else:
    return "[%s](http://coingecko.com/en/coins/%s)" % (name, coingecko_id)


def _link_source_address(source_chain, source_addr):
  source_contract = "%s/address/%s" % (SOURCE_INFO[source_chain][2] , source_addr)
  return "[%s](%s)" % (source_addr, source_contract)


def gen_markdown(dest):
  dest_full = SOURCE_INFO[dest][0]
  tokens = {}
  for coin, entry in TOKENS.items():
    if dest not in entry['destAddresses']:
      continue
    entry = copy.deepcopy(entry)
    entry['address'] = entry['destAddresses'][dest]
    entry.pop('destAddresses')
    tokens[coin] = entry
  df = pd.DataFrame(tokens.values())
  if df.shape[0] == 0:
    print('no tokens for dest=%s' % dest)
    return
  df = df.sort_values(by='symbol')
  df['name'] = [_link_coingecko(n, c) for (n, c) in zip(df['name'].values, df['coingeckoId'].values)]
  df['address'] = [_link_address(dest, x) for x in df['address'].values]
  df['sourceAddress'] = [_link_source_address(x, y) for (x,y) in
                         zip(df['origin'].values, df['sourceAddress'].values)]
  df['origin'] = [SOURCE_INFO[x][0].lower() for x in df['origin'].values]
  df['symbol_reprise'] = df['symbol']

  df = df.drop(['coingeckoId'], axis=1)

  df = df[['symbol', 'name', 'address', 'origin', 'sourceAddress', 'symbol_reprise']]

  # col_rename = {
  # }
  # df.columns = [col_rename.get(x, x) for x in df.columns]

  txt = df.to_markdown(index=False).replace('symbol_reprise', 'symbol')
  header = """
Known tokens (wormholed to %s)
===================================
  """ % dest_full
  outpath = os.path.join(dir_path, 'dest_%s.md' % dest_full.lower())
  with open(outpath, 'w') as f:
    f.write(header + '\n' + txt)
  print('wrote %s' % outpath)


if __name__ == "__main__":
  for dest in ['eth', 'bsc', 'terra', 'avax', 'matic']:
    gen_markdown(dest)