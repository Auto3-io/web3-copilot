.. _addresses-overview:

====================
Deployment Addresses
====================

Here is a list of all current contract deployments within the Curve protocol.

.. note::

    If you find an address which is missing or incorrect, feel free to create a pull request as specified `here <https://github.com/curvefi/curve-docs>`_.

Base Pools
==========

Base pools in Curve contain two or more tokens and implement the  `Curve stable swap exchange mechanism <https://www.curve.fi/stableswap-paper.pdf>`_. Note that for a single base or meta pool there are multiple deployed contracts, which are of the following formats:

- ``StableSwap<pool>.vy``: Curve stablecoin AMM contract
- ``Deposit<pool>.vy``: contract used to wrap underlying tokens prior to depositing them into the pool (not always required)
- ``CurveContract<version>.vy``: LP token contract for the pool

Here is a list of all base pool contracts currently in use:

.. csv-table::
   :header: "Pool", "Source", "Address"

   3Pool, `StableSwap3Pool.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/3pool/StableSwap3Pool.vy>`_, `0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7 <https://etherscan.io/address/0xbebc44782c7db0a1a60cb6fe97d0b483032ff1c7#code>`_
   3Pool, `CurveTokenV2.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV2.vy>`_, `0x6c3F90f043a72FA612cbac8115EE7e52BDe6E490 <https://etherscan.io/address/0x6c3F90f043a72FA612cbac8115EE7e52BDe6E490#code>`_
   AAVE, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_, `0xFd2a8fA60Abd58Efe3EeE34dd494cD491dC14900 <https://etherscan.io/address/0xFd2a8fA60Abd58Efe3EeE34dd494cD491dC14900#code>`_
   AAVE, `StableSwapAave.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/aave/StableSwapAave.vy>`_, `0xDeBF20617708857ebe4F679508E7b7863a8A8EeE <https://etherscan.io/address/0xDeBF20617708857ebe4F679508E7b7863a8A8EeE#code>`_
   ankrETH, `StableSwapAETH.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/aeth/StableSwapAETH.vy>`_, `0xA96A65c051bF88B4095Ee1f2451C2A9d43F53Ae2 <https://etherscan.io/address/0xA96A65c051bF88B4095Ee1f2451C2A9d43F53Ae2#code>`_
   ankrETH, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_, `0xaA17A236F2bAdc98DDc0Cf999AbB47D47Fc0A6Cf <https://etherscan.io/address/0xaA17A236F2bAdc98DDc0Cf999AbB47D47Fc0A6Cf#code>`_
   BUSD, `StableSwapBUSD.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/busd/StableSwapBUSD.vy>`_, `0x79a8C46DeA5aDa233ABaFFD40F3A0A2B1e5A4F27 <https://etherscan.io/address/0x79a8C46DeA5aDa233ABaFFD40F3A0A2B1e5A4F27#code>`_
   BUSD, `DepositBUSD.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/busd/DepositBUSD.vy>`_, `0xb6c057591E073249F2D9D88Ba59a46CFC9B59EdB <https://etherscan.io/address/0xb6c057591e073249f2d9d88ba59a46cfc9b59edb#code>`_
   BUSD, `CurveTokenV1.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV1.vy>`_, `0x3B3Ac5386837Dc563660FB6a0937DFAa5924333B <https://etherscan.io/address/0x3B3Ac5386837Dc563660FB6a0937DFAa5924333B#code>`_
   Compound, `StableSwapCompound.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/compound/StableSwapCompound.vy>`_, `0xA2B47E3D5c44877cca798226B7B8118F9BFb7A56 <https://etherscan.io/address/0xA2B47E3D5c44877cca798226B7B8118F9BFb7A56#code>`_
   Compound, `DepositCompound.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/compound/DepositCompound.vy>`_, `0xeB21209ae4C2c9FF2a86ACA31E123764A3B6Bc06 <https://etherscan.io/address/0xeb21209ae4c2c9ff2a86aca31e123764a3b6bc06#code>`_
   Compound, `CurveContractV1.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV1.vy>`_, `0x845838DF265Dcd2c412A1Dc9e959c7d08537f8a2 <https://etherscan.io/address/0x845838DF265Dcd2c412A1Dc9e959c7d08537f8a2#code>`_
   EURS, `StableSwapEURS.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/eurs/StableSwapEURS.vy>`_, `0x0Ce6a5fF5217e38315f87032CF90686C96627CAA <https://etherscan.io/address/0x0Ce6a5fF5217e38315f87032CF90686C96627CAA#code>`_
   EURS, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_, `0x194eBd173F6cDacE046C53eACcE9B953F28411d1 <https://etherscan.io/address/0x194eBd173F6cDacE046C53eACcE9B953F28411d1#code>`_
   hBTC, `StableSwapHBTC.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/hbtc/StableSwapHBTC.vy>`_, `0x4CA9b3063Ec5866A4B82E437059D2C43d1be596F <https://etherscan.io/address/0x4CA9b3063Ec5866A4B82E437059D2C43d1be596F#code>`_
   hBTC, `CurveTokenV2.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV2.vy>`_, `0xb19059ebb43466C323583928285a49f558E572Fd <https://etherscan.io/address/0xb19059ebb43466C323583928285a49f558E572Fd#code>`_
   IronBank, `StableSwapIB.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/ib/StableSwapIB.vy>`_, `0x2dded6Da1BF5DBdF597C45fcFaa3194e53EcfeAF <https://etherscan.io/address/0x2dded6Da1BF5DBdF597C45fcFaa3194e53EcfeAF#code>`_
   IronBank, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_, `0x5282a4eF67D9C33135340fB3289cc1711c13638C <https://etherscan.io/address/0x5282a4eF67D9C33135340fB3289cc1711c13638C#code>`_
   Link, `StableSwapLINK.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/link/StableSwapLINK.vy>`_, `0xF178C0b5Bb7e7aBF4e12A4838C7b7c5bA2C623c0 <https://etherscan.io/address/0xF178C0b5Bb7e7aBF4e12A4838C7b7c5bA2C623c0#code>`_
   Link, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_, `0xcee60cfa923170e4f8204ae08b4fa6a3f5656f3a <https://etherscan.io/address/0xcee60cfa923170e4f8204ae08b4fa6a3f5656f3a#code>`_
   PAX, `DepositPax.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/pax/DepositPax.vy>`_, `0xA50cCc70b6a011CffDdf45057E39679379187287 <https://etherscan.io/address/0xa50ccc70b6a011cffddf45057e39679379187287#code>`_
   PAX, `StableSwapPax.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/pax/StableSwapPax.vy>`_, `0x06364f10B501e868329afBc005b3492902d6C763 <https://etherscan.io/address/0x06364f10B501e868329afBc005b3492902d6C763#code>`_
   PAX, `CurveTokenV1.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV1.vy>`_, `0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8 <https://etherscan.io/address/0xD905e2eaeBe188fc92179b6350807D8bd91Db0D8#code>`_
   renBTC, `StableSwapRen.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/ren/StableSwapRen.vy>`_, `0x93054188d876f558f4a66B2EF1d97d16eDf0895B <https://etherscan.io/address/0x93054188d876f558f4a66B2EF1d97d16eDf0895B#code>`_
   renBTC, `CurveTokenV1.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV1.vy>`_, `0x49849C98ae39Fff122806C06791Fa73784FB3675 <https://etherscan.io/address/0x49849C98ae39Fff122806C06791Fa73784FB3675#code>`_
   rETH, `StableSwapRETH.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/reth/StableSwapRETH.vy>`_, `0xF9440930043eb3997fc70e1339dBb11F341de7A8 <https://etherscan.io/address/0xF9440930043eb3997fc70e1339dBb11F341de7A8#code>`_
   rETH, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_, `0x53a901d48795C58f485cBB38df08FA96a24669D5 <https://etherscan.io/address/0x53a901d48795C58f485cBB38df08FA96a24669D5#code>`_
   sAAVE, `StableSwapSAAVE.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/saave/StableSwapSAAVE.vy>`_, `0xEB16Ae0052ed37f479f7fe63849198Df1765a733 <https://etherscan.io/address/0xeb16ae0052ed37f479f7fe63849198df1765a733#code>`_
   sAAVE, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_, `0x02d341CcB60fAaf662bC0554d13778015d1b285C <https://etherscan.io/address/0x02d341CcB60fAaf662bC0554d13778015d1b285C#code>`_
   sBTC, `StableSwapSBTC.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/sbtc/StableSwapSBTC.vy>`_, `0x7fC77b5c7614E1533320Ea6DDc2Eb61fa00A9714 <https://etherscan.io/address/0x7fC77b5c7614E1533320Ea6DDc2Eb61fa00A9714#code>`_
   sBTC, `CurveTokenV1.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV1.vy>`_,`0x075b1bb99792c9E1041bA13afEf80C91a1e70fB3 <https://etherscan.io/address/0x075b1bb99792c9E1041bA13afEf80C91a1e70fB3#code>`_
   sETH, `StableSwapSETH.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/seth/StableSwapSETH.vy>`_, `0xc5424B857f758E906013F3555Dad202e4bdB4567 <https://etherscan.io/address/0xc5424b857f758e906013f3555dad202e4bdb4567#code>`_
   sETH, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_, `0xA3D87FffcE63B53E0d54fAa1cc983B7eB0b74A9c <https://etherscan.io/address/0xA3D87FffcE63B53E0d54fAa1cc983B7eB0b74A9c#code>`_
   stETH, `StableSwapSTETH.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/steth/StableSwapSTETH.vy>`_, `0xDC24316b9AE028F1497c275EB9192a3Ea0f67022 <https://etherscan.io/address/0xDC24316b9AE028F1497c275EB9192a3Ea0f67022#code>`_
   stETH, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_, `0x06325440D014e39736583c165C2963BA99fAf14E <https://etherscan.io/address/0x06325440D014e39736583c165C2963BA99fAf14E#code>`_
   sUSD, `DepositSUSD.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/susd/DepositSUSD.vy>`_, `0xFCBa3E75865d2d561BE8D220616520c171F12851 <https://etherscan.io/address/0xfcba3e75865d2d561be8d220616520c171f12851#code>`_
   sUSD, `StableSwapSUSD.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/susd/StableSwapSUSD.vy>`_, `0xA5407eAE9Ba41422680e2e00537571bcC53efBfD <https://etherscan.io/address/0xA5407eAE9Ba41422680e2e00537571bcC53efBfD#code>`_
   sUSD, `CurveTokenV1.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV1.vy>`_, `0xC25a3A3b969415c80451098fa907EC722572917F <https://etherscan.io/address/0xC25a3A3b969415c80451098fa907EC722572917F#code>`_
   TriCrypto, `CurveCryptoSwap.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/contracts/CurveCryptoSwap.vy>`_, `0x80466c64868E1ab14a1Ddf27A676C3fcBE638Fe5 <https://etherscan.io/address/0x80466c64868E1ab14a1Ddf27A676C3fcBE638Fe5#code>`_
   TriCrypto, `DepositZap.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/contracts/DepositZap.vy>`_, `0x331aF2E331bd619DefAa5DAc6c038f53FCF9F785 <https://etherscan.io/address/0x331aF2E331bd619DefAa5DAc6c038f53FCF9F785#code>`_
   TriCrypto, `CurveTokenV4.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/contracts/CurveTokenV4.vy>`_, `0xcA3d75aC011BF5aD07a98d02f18225F9bD9A6BDF <https://etherscan.io/address/0xcA3d75aC011BF5aD07a98d02f18225F9bD9A6BDF#code>`_
   USDT, `DepositUSDT.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/usdt/DepositUSDT.vy>`_, `0xac795D2c97e60DF6a99ff1c814727302fD747a80 <https://etherscan.io/address/0xac795d2c97e60df6a99ff1c814727302fd747a80#code>`_
   USDT, `StableSwapUSDT.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/usdt/StableSwapUSDT.vy>`_, `0x52EA46506B9CC5Ef470C5bf89f17Dc28bB35D85C <https://etherscan.io/address/0x52EA46506B9CC5Ef470C5bf89f17Dc28bB35D85C#code>`_
   USDT, `CurveTokenV1.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV1.vy>`_, `0x9fC689CCaDa600B6DF723D9E47D84d76664a1F23 <https://etherscan.io/address/0x9fC689CCaDa600B6DF723D9E47D84d76664a1F23#code>`_
   Y, `DepositY.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/y/DepositY.vy>`_, `0xbBC81d23Ea2c3ec7e56D39296F0cbB648873a5d3 <https://etherscan.io/address/0xbbc81d23ea2c3ec7e56d39296f0cbb648873a5d3#code>`_
   Y, `StableSwapY.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/y/StableSwapY.vy>`_, `0x45F783CCE6B7FF23B2ab2D70e416cdb7D6055f51 <https://etherscan.io/address/0x45F783CCE6B7FF23B2ab2D70e416cdb7D6055f51#code>`_
   Y, `CurveTokenV1.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV1.vy>`_, `0xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8 <https://etherscan.io/address/0xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8#code>`_
   Yv2, `StableSwapYv2.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/yv2/StableSwapYv2.vy>`_, `0x8925D9d9B4569D737a48499DeF3f67BaA5a144b9 <https://etherscan.io/address/0x8925D9d9B4569D737a48499DeF3f67BaA5a144b9#code>`_
   Yv2, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_, `0x571FF5b7b346F706aa48d696a9a4a288e9Bb4091 <https://etherscan.io/address/0x571FF5b7b346F706aa48d696a9a4a288e9Bb4091#code>`_

.. _addresses-metapools:

MetaPools
==========

Metapools allow for one token to seemingly trade with another underlying base pool. For instance, the GUSD metapool (``[GUSD, [3Pool]]``) contains GUSD and LP tokens of the 3pool (3CRV). This allows for trades between GUSD and any of the three tokens from the 3Pool (DAI, USDC and USDT).

Here is a list of all meta pools currently in use:

.. csv-table::
   :header: "Pool", "Source", "Address"

   bBTC, `StableSwapBBTC.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/bbtc/StableSwapBBTC.vy>`_, `0x071c661B4DeefB59E2a3DdB20Db036821eeE8F4b <https://etherscan.io/address/0x071c661B4DeefB59E2a3DdB20Db036821eeE8F4b#code>`_
   bBTC, `DepositBBTC.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/bbtc/DepositBBTC.vy>`_, `0xC45b2EEe6e09cA176Ca3bB5f7eEe7C47bF93c756 <https://etherscan.io/address/0xC45b2EEe6e09cA176Ca3bB5f7eEe7C47bF93c756#code>`_
   bBTC, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_, `0x410e3E86ef427e30B9235497143881f717d93c2A <https://etherscan.io/address/0x410e3E86ef427e30B9235497143881f717d93c2A#code>`_
   DUSD, `DepositDUSD.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/dusd/DepositDUSD.vy>`_, `0x61E10659fe3aa93d036d099405224E4Ac24996d0 <https://etherscan.io/address/0x61E10659fe3aa93d036d099405224E4Ac24996d0#code>`_
   DUSD, `StableSwapDUSD.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/dusd/StableSwapDUSD.vy>`_, `0x8038C01A0390a8c547446a0b2c18fc9aEFEcc10c <https://etherscan.io/address/0x8038C01A0390a8c547446a0b2c18fc9aEFEcc10c#code>`_
   DUSD, `CurveTokenV2.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV2.vy>`_, `0x3a664Ab939FD8482048609f652f9a0B0677337B9 <https://etherscan.io/address/0x3a664Ab939FD8482048609f652f9a0B0677337B9#code>`_
   GUSD, `StableSwapGUSD.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/gusd/StableSwapGUSD.vy>`_, `0x4f062658EaAF2C1ccf8C8e36D6824CDf41167956 <https://etherscan.io/address/0x4f062658EaAF2C1ccf8C8e36D6824CDf41167956>`_
   GUSD, `DepositGUSD.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/gusd/DepositGUSD.vy>`_, `0x64448B78561690B70E17CBE8029a3e5c1bB7136e <https://etherscan.io/address/0x64448B78561690B70E17CBE8029a3e5c1bB7136e#code>`_
   GUSD, `CurveTokenV2.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV2.vy>`_, `0xD2967f45c4f384DEEa880F807Be904762a3DeA07 <https://etherscan.io/address/0xD2967f45c4f384DEEa880F807Be904762a3DeA07#code>`_
   HUSD, `DepositHUSD.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/husd/DepositHUSD.vy>`_, `0x09672362833d8f703D5395ef3252D4Bfa51c15ca <https://etherscan.io/address/0x09672362833d8f703D5395ef3252D4Bfa51c15ca#code>`_
   HUSD, `StableSwapHUSD.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/husd/StableSwapHUSD.vy>`_, `0x3eF6A01A0f81D6046290f3e2A8c5b843e738E604 <https://etherscan.io/address/0x3eF6A01A0f81D6046290f3e2A8c5b843e738E604#code>`_
   HUSD, `CurveTokenV2.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV2.vy>`_, `0x5B5CFE992AdAC0C9D48E05854B2d91C73a003858 <https://etherscan.io/address/0x5B5CFE992AdAC0C9D48E05854B2d91C73a003858#code>`_
   LinkUSD, `DepositLinkUSD.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/linkusd/DepositLinkUSD.vy>`_, `0x1de7f0866e2c4adAC7b457c58Cc25c8688CDa1f2 <https://etherscan.io/address/0x1de7f0866e2c4adAC7b457c58Cc25c8688CDa1f2#code>`_
   LinkUSD, `StableSwapLinkUSD.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/linkusd/StableSwapLinkUSD.vy>`_, `0xE7a24EF0C5e95Ffb0f6684b813A78F2a3AD7D171 <https://etherscan.io/address/0xE7a24EF0C5e95Ffb0f6684b813A78F2a3AD7D171#code>`_
   LinkUSD, `CurveTokenV2.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV2.vy>`_, `0x6D65b498cb23deAba52db31c93Da9BFFb340FB8F <https://etherscan.io/address/0x6D65b498cb23deAba52db31c93Da9BFFb340FB8F#code>`_
   MUSD, `DepositMUSD.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/musd/DepositMUSD.vy>`_, `0x803A2B40c5a9BB2B86DD630B274Fa2A9202874C2 <https://etherscan.io/address/0x803A2B40c5a9BB2B86DD630B274Fa2A9202874C2#code>`_
   MUSD, `StableSwapMUSD.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/musd/StableSwapMUSD.vy>`_, `0x8474DdbE98F5aA3179B3B3F5942D724aFcdec9f6 <https://etherscan.io/address/0x8474DdbE98F5aA3179B3B3F5942D724aFcdec9f6#code>`_
   MUSD, `CurveTokenV2.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV2.vy>`_, `0x1AEf73d49Dedc4b1778d0706583995958Dc862e6 <https://etherscan.io/address/0x1AEf73d49Dedc4b1778d0706583995958Dc862e6#code>`_
   oBTC, `DepositOBTC.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/obtc/DepositOBTC.vy>`_, `0xd5BCf53e2C81e1991570f33Fa881c49EEa570C8D <https://etherscan.io/address/0xd5BCf53e2C81e1991570f33Fa881c49EEa570C8D#code>`_
   oBTC, `StableSwapOBTC.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/obtc/StableSwapOBTC.vy>`_, `0xd81dA8D904b52208541Bade1bD6595D8a251F8dd <https://etherscan.io/address/0xd81dA8D904b52208541Bade1bD6595D8a251F8dd#code>`_
   oBTC, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_, `0x2fE94ea3d5d4a175184081439753DE15AeF9d614 <https://etherscan.io/address/0x2fE94ea3d5d4a175184081439753DE15AeF9d614#code>`_
   pBTC, `DepositPBTC.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/pbtc/DepositPBTC.vy>`_,`0x11F419AdAbbFF8d595E7d5b223eee3863Bb3902C <https://etherscan.io/address/0x11F419AdAbbFF8d595E7d5b223eee3863Bb3902C#code>`_
   pBTC, `StableSwapPBTC.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/pbtc/StableSwapPBTC.vy>`_, `0x7F55DDe206dbAD629C080068923b36fe9D6bDBeF <https://etherscan.io/address/0x7F55DDe206dbAD629C080068923b36fe9D6bDBeF#code>`_
   pBTC, `CurveTokenV2.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV2.vy>`_, `0xDE5331AC4B3630f94853Ff322B66407e0D6331E8 <https://etherscan.io/address/0xDE5331AC4B3630f94853Ff322B66407e0D6331E8#code>`_
   RSV, `DepositRSV.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/rsv/DepositRSV.vy>`_, `0xBE175115BF33E12348ff77CcfEE4726866A0Fbd5 <https://etherscan.io/address/0xBE175115BF33E12348ff77CcfEE4726866A0Fbd5#code>`_
   RSV, `StableSwapRSV.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/rsv/StableSwapRSV.vy>`_, `0xC18cC39da8b11dA8c3541C598eE022258F9744da <https://etherscan.io/address/0xC18cC39da8b11dA8c3541C598eE022258F9744da#code>`_
   RSV, `CurveTokenV2.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV2.vy>`_, `0xC2Ee6b0334C261ED60C72f6054450b61B8f18E35 <https://etherscan.io/address/0xC2Ee6b0334C261ED60C72f6054450b61B8f18E35#code>`_
   tBTC, `DepositTBTC.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/tbtc/DepositTBTC.vy>`_, `0xaa82ca713D94bBA7A89CEAB55314F9EfFEdDc78c <https://etherscan.io/address/0xaa82ca713D94bBA7A89CEAB55314F9EfFEdDc78c#code>`_
   tBTC, `StableSwapTBTC.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/tbtc/StableSwapTBTC.vy>`_, `0xC25099792E9349C7DD09759744ea681C7de2cb66 <https://etherscan.io/address/0xC25099792E9349C7DD09759744ea681C7de2cb66#code>`_
   tBTC, `CurveTokenV2.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV2.vy>`_, `0x64eda51d3Ad40D56b9dFc5554E06F94e1Dd786Fd <https://etherscan.io/address/0x64eda51d3Ad40D56b9dFc5554E06F94e1Dd786Fd#code>`_
   USDK, `DepositUSDK.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/usdk/DepositUSDK.vy>`_, `0xF1f85a74AD6c64315F85af52d3d46bF715236ADc <https://etherscan.io/address/0xF1f85a74AD6c64315F85af52d3d46bF715236ADc#code>`_
   USDK, `StableSwapUSDK.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/usdk/StableSwapUSDK.vy>`_, `0x3E01dD8a5E1fb3481F0F589056b428Fc308AF0Fb <https://etherscan.io/address/0x3E01dD8a5E1fb3481F0F589056b428Fc308AF0Fb#code>`_
   USDK, `CurveTokenV2.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV2.vy>`_, `0x97E2768e8E73511cA874545DC5Ff8067eB19B787 <https://etherscan.io/address/0x97E2768e8E73511cA874545DC5Ff8067eB19B787#code>`_
   USDN, `DepositUSDN.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/usdn/DepositUSDN.vy>`_, `0x094d12e5b541784701FD8d65F11fc0598FBC6332 <https://etherscan.io/address/0x094d12e5b541784701FD8d65F11fc0598FBC6332#code>`_
   USDN, `StableSwapUSDN.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/usdn/StableSwapUSDN.vy>`_, `0x0f9cb53Ebe405d49A0bbdBD291A65Ff571bC83e1 <https://etherscan.io/address/0x0f9cb53Ebe405d49A0bbdBD291A65Ff571bC83e1#code>`_
   USDN, `CurveTokenV2.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV2.vy>`_, `0x4f3E8F405CF5aFC05D68142F3783bDfE13811522 <https://etherscan.io/address/0x4f3E8F405CF5aFC05D68142F3783bDfE13811522#code>`_
   USDP, `DepositUSDP.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/usdp/DepositUSDP.vy>`_, `0x3c8cAee4E09296800f8D29A68Fa3837e2dae4940 <https://etherscan.io/address/0x3c8cAee4E09296800f8D29A68Fa3837e2dae4940#code>`_
   USDP, `StableSwapUSDP.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/usdp/StableSwapUSDP.vy>`_, `0x42d7025938bEc20B69cBae5A77421082407f053A <https://etherscan.io/address/0x42d7025938bEc20B69cBae5A77421082407f053A#code>`_
   USDP, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_, `0x7Eb40E450b9655f4B3cC4259BCC731c63ff55ae6 <https://etherscan.io/address/0x7Eb40E450b9655f4B3cC4259BCC731c63ff55ae6#code>`_
   UST, `DepositUST.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/ust/DepositUST.vy>`_, `0xB0a0716841F2Fc03fbA72A891B8Bb13584F52F2d <https://etherscan.io/address/0xB0a0716841F2Fc03fbA72A891B8Bb13584F52F2d#code>`_
   UST, `StableSwapUST.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/pools/ust/StableSwapUST.vy>`_, `0x890f4e345B1dAED0367A877a1612f86A1f86985f <https://etherscan.io/address/0x890f4e345B1dAED0367A877a1612f86A1f86985f#code>`_
   UST, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/tokens/CurveTokenV3.vy>`_, `0x94e131324b6054c0D789b190b2dAC504e4361b53 <https://etherscan.io/address/0x94e131324b6054c0D789b190b2dAC504e4361b53#code>`_


.. _addresses-gauges:

Liquidity Gauges
================

Liquidity Gauges are used to stake LP tokens and handle distribution of the CRV governance token and are part of the Curve DAO.

Here is a list of all liquidity gauges currently in use:

.. csv-table::
   :header: "Gauge", "Source", "Address"

   3pool, `LiquidityGauge.sol <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGauge.vy>`_, `0xbFcF63294aD7105dEa65aA58F8AE5BE2D9d0952A <https://etherscan.io/address/0xbFcF63294aD7105dEa65aA58F8AE5BE2D9d0952A#code>`_
   AAVE, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0xd662908ADA2Ea1916B3318327A97eB18aD588b5d <https://etherscan.io/address/0xd662908ADA2Ea1916B3318327A97eB18aD588b5d#code>`_
   alUSD, `LiquidityGaugeV3.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV3.vy>`_, `0x9582C4ADACB3BCE56Fea3e590F05c3ca2fb9C477 <https://etherscan.io/address/0x9582C4ADACB3BCE56Fea3e590F05c3ca2fb9C477#code>`_
   ankrETH, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0x6d10ed2cF043E6fcf51A0e7b4C2Af3Fa06695707 <https://etherscan.io/address/0x6d10ed2cF043E6fcf51A0e7b4C2Af3Fa06695707#code>`_
   bBTC, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0xdFc7AdFa664b08767b735dE28f9E84cd30492aeE <https://etherscan.io/address/0xdFc7AdFa664b08767b735dE28f9E84cd30492aeE#code>`_
   BUSD, `LiquidityGauge.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGauge.vy>`_, `0x69Fb7c45726cfE2baDeE8317005d3F94bE838840 <https://etherscan.io/address/0x69Fb7c45726cfE2baDeE8317005d3F94bE838840#code>`_
   Compound, `LiquidityGauge.sol <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGauge.vy>`_, `0x7ca5b0a2910B33e9759DC7dDB0413949071D7575 <https://etherscan.io/address/0x7ca5b0a2910B33e9759DC7dDB0413949071D7575#code>`_
   DUSD, `LiquidityGaugeReward.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGaugeReward.vy>`_, `0xAEA6c312f4b3E04D752946d329693F7293bC2e6D <https://etherscan.io/address/0xAEA6c312f4b3E04D752946d329693F7293bC2e6D#code>`_
   EURS, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0x90Bb609649E0451E5aD952683D64BD2d1f245840 <https://etherscan.io/address/0x90Bb609649E0451E5aD952683D64BD2d1f245840#code>`_
   FRAX, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0x72e158d38dbd50a483501c24f792bdaaa3e7d55c <https://etherscan.io/address/0x72e158d38dbd50a483501c24f792bdaaa3e7d55c#code>`_
   GUSD, `LiquidityGauge.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGauge.vy>`_, `0xC5cfaDA84E902aD92DD40194f0883ad49639b023 <https://etherscan.io/address/0xC5cfaDA84E902aD92DD40194f0883ad49639b023#code>`_
   hBTC, `LiquidityGauge.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGauge.vy>`_, `0x4c18E409Dc8619bFb6a1cB56D114C3f592E0aE79 <https://etherscan.io/address/0x4c18E409Dc8619bFb6a1cB56D114C3f592E0aE79#code>`_
   HUSD, `LiquidityGauge.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGauge.vy>`_, `0x2db0E83599a91b508Ac268a6197b8B14F5e72840 <https://etherscan.io/address/0x2db0E83599a91b508Ac268a6197b8B14F5e72840#code>`_
   MUSD, `LiquidityGaugeReward.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGaugeReward.vy>`_, `0x5f626c30EC1215f4EdCc9982265E8b1F411D1352 <https://etherscan.io/address/0x5f626c30EC1215f4EdCc9982265E8b1F411D1352#code>`_
   oBTC, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0x11137B10C210b579405c21A07489e28F3c040AB1 <https://etherscan.io/address/0x11137B10C210b579405c21A07489e28F3c040AB1#code>`_
   PAX, `LiquidityGauge.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGauge.vy>`_, `0x64E3C23bfc40722d3B649844055F1D51c1ac041d <https://etherscan.io/address/0x64E3C23bfc40722d3B649844055F1D51c1ac041d#code>`_
   IronBank, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0xF5194c3325202F456c95c1Cf0cA36f8475C1949F <https://etherscan.io/address/0xF5194c3325202F456c95c1Cf0cA36f8475C1949F#code>`_
   Link, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0xFD4D8a17df4C27c1dD245d153ccf4499e806C87D <https://etherscan.io/address/0xFD4D8a17df4C27c1dD245d153ccf4499e806C87D#code>`_
   pBTC, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0xd7d147c6Bb90A718c3De8C0568F9B560C79fa416 <https://etherscan.io/address/0xd7d147c6Bb90A718c3De8C0568F9B560C79fa416#code>`_
   renBTC, `LiquidityGauge.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGauge.vy>`_, `0xB1F2cdeC61db658F091671F5f199635aEF202CAC <https://etherscan.io/address/0xB1F2cdeC61db658F091671F5f199635aEF202CAC#code>`_
   RSV, `LiquidityGaugeReward.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGaugeReward.vy>`_, `0x4dC4A289a8E33600D8bD4cf5F6313E43a37adec7 <https://etherscan.io/address/0x4dC4A289a8E33600D8bD4cf5F6313E43a37adec7#code>`_
   sAAVE, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0x462253b8F74B72304c145DB0e4Eebd326B22ca39 <https://etherscan.io/address/0x462253b8F74B72304c145DB0e4Eebd326B22ca39#code>`_
   sBTC, `LiquidityGaugeReward.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGaugeReward.vy>`_, `0x705350c4BcD35c9441419DdD5d2f097d7a55410F <https://etherscan.io/address/0x705350c4BcD35c9441419DdD5d2f097d7a55410F#code>`_
   sETH, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0x3C0FFFF15EA30C35d7A85B85c0782D6c94e1d238 <https://etherscan.io/address/0x3C0FFFF15EA30C35d7A85B85c0782D6c94e1d238#code>`_
   stETH, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0x182B723a58739a9c974cFDB385ceaDb237453c28 <https://etherscan.io/address/0x182B723a58739a9c974cFDB385ceaDb237453c28#code>`_
   sUSDv2, `LiquidityGaugeReward.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGaugeReward.vy>`_, `0xA90996896660DEcC6E997655E065b23788857849 <https://etherscan.io/address/0xA90996896660DEcC6E997655E065b23788857849#code>`_
   rETH, `LiquidityGaugeV3.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV3.vy>`_, `0x824F13f1a2F29cFEEa81154b46C0fc820677A637 <https://etherscan.io/address/0x824F13f1a2F29cFEEa81154b46C0fc820677A637#code>`_
   tBTC, `LiquidityGaugeReward.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGaugeReward.vy>`_, `0x6828bcF74279eE32f2723eC536c22c51Eed383C6 <https://etherscan.io/address/0x6828bcF74279eE32f2723eC536c22c51Eed383C6#code>`_
   TriCrypto, `LiquidityGaugeV3.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV3.vy>`_, `0x6955a55416a06839309018A8B0cB72c4DDC11f15 <https://etherscan.io/address/0x6955a55416a06839309018A8B0cB72c4DDC11f15#code>`_
   USDK, `LiquidityGauge.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGauge.vy>`_, `0xC2b1DF84112619D190193E48148000e3990Bf627 <https://etherscan.io/address/0xC2b1DF84112619D190193E48148000e3990Bf627#code>`_
   USDN, `LiquidityGauge.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGauge.vy>`_, `0xF98450B5602fa59CC66e1379DFfB6FDDc724CfC4 <https://etherscan.io/address/0xF98450B5602fa59CC66e1379DFfB6FDDc724CfC4#code>`_
   USDP, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0x055be5DDB7A925BfEF3417FC157f53CA77cA7222 <https://etherscan.io/address/0x055be5DDB7A925BfEF3417FC157f53CA77cA7222#code>`_
   USDT, `LiquidityGauge.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGauge.vy>`_, `0xBC89cd85491d81C6AD2954E6d0362Ee29fCa8F53 <https://etherscan.io/address/0xBC89cd85491d81C6AD2954E6d0362Ee29fCa8F53#code>`_
   UST, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0x3B7020743Bc2A4ca9EaF9D0722d42E20d6935855 <https://etherscan.io/address/0x3B7020743Bc2A4ca9EaF9D0722d42E20d6935855#code>`_
   Y, `LiquidityGauge.vy <https://github.com/curvefi/curve-contract/blob/master/contracts/gauges/LiquidityGauge.vy>`_, `0xFA712EE4788C042e2B7BB55E6cb8ec569C4530c1 <https://etherscan.io/address/0xFA712EE4788C042e2B7BB55E6cb8ec569C4530c1#code>`_
   Yv2, `LiquidityGaugeV2.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/LiquidityGaugeV2.vy>`_, `0x8101E6760130be2C8Ace79643AB73500571b7162 <https://etherscan.io/address/0x8101E6760130be2C8Ace79643AB73500571b7162#code>`_

.. _addresses-dao:

Curve DAO
=========

Curve DAO consists of multiple smart contracts connected by `Aragon <https://github.com/aragon/aragonOS>`_. Interaction with Aragon occurs through a `modified implementation <https://github.com/curvefi/curve-aragon-voting>`_ of the `Aragon Voting App <https://github.com/aragon/aragon-apps/tree/master/apps/voting>`_. Aragon's standard one token, one vote method is replaced with a weighting system based on locking tokens. Curve DAO has a token (CRV) which is used for both governance and value accrual.

View the `documentation <https://github.com/curvefi/curve-dao-contracts/blob/master/doc/readme.pdf>`_ for an in-depth overview of how the Curve DAO works.

Here is a list of contract deployments that are used in the Curve DAO:

.. csv-table::
   :header: "Name", "Source", "Address"

   CRV Token, `ERC20CRV.sol <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/ERC20CRV.vy>`_, `0xD533a949740bb3306d119CC777fa900bA034cd52 <https://etherscan.io/address/0xD533a949740bb3306d119CC777fa900bA034cd52#code>`_
   Fee Distributor, `FeeDistributor.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/FeeDistributor.vy>`_, `0xA464e6DCda8AC41e03616F95f4BC98a13b8922Dc <https://etherscan.io/address/0xA464e6DCda8AC41e03616F95f4BC98a13b8922Dc#code>`_
   Gauge Controller, `GaugeController.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/GaugeController.vy>`_, `0x2F50D538606Fa9EDD2B11E2446BEb18C9D5846bB <https://etherscan.io/address/0x2F50D538606Fa9EDD2B11E2446BEb18C9D5846bB#code>`_
   Minter, `Minter.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/Minter.vy>`_, `0xd061D61a4d941c39E5453435B6345Dc261C2fcE0 <https://etherscan.io/address/0xd061D61a4d941c39E5453435B6345Dc261C2fcE0#code>`_
   Voting Escrow, `VotingEscrow.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/VotingEscrow.vy>`_, `0x5f3b5DfEb7B28CDbD7FAba78963EE202a494e2A2 <https://etherscan.io/address/0x5f3b5DfEb7B28CDbD7FAba78963EE202a494e2A2#code>`_
   Vesting Escrow, `VestingEscrow.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/VestingEscrow.vy>`_, `0x575ccd8e2d300e2377b43478339e364000318e2c <https://etherscan.io/address/0x575ccd8e2d300e2377b43478339e364000318e2c#code>`_

Ownership Proxies
-----------------

The following contracts allow DAO ownership of the core Curve AMM contracts:

.. csv-table::
   :header: "Name", "Source", "Address"

   Gauge Owner, `GaugeProxy.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/GaugeProxy.vy>`_, `0x519AFB566c05E00cfB9af73496D00217A630e4D5 <https://etherscan.io/address/0x519AFB566c05E00cfB9af73496D00217A630e4D5#code>`_
   Pool Owner, `PoolProxy.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/PoolProxy.vy>`_, `0xeCb456EA5365865EbAb8a2661B0c503410e9B347 <https://etherscan.io/address/0xeCb456EA5365865EbAb8a2661B0c503410e9B347#code>`_
   Crypto Pool Owner, `CryptoPoolProxy.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/CryptoPoolProxy.vy>`_, `0x3687367CcAEBBE89f1bc8Eae7592b4Eed44Ac0Bd <https://etherscan.io/address/0x3687367ccaebbe89f1bc8eae7592b4eed44ac0bd>`_
   Factory Pool Owner, `OwnerProxy.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/OwnerProxy.vy>`_, `0x8cf8af108b3b46ddc6ad596aebb917e053f0d72b <https://etherscan.io/address/0x8cf8af108b3b46ddc6ad596aebb917e053f0d72b>`_


.. _addresses-aragon:

Aragon
------

Main documentation: :ref:`Curve DAO: Governance<dao-voting>`

Voting App
**********

Aragon `Voting App <https://wiki.aragon.org/archive/dev/apps/voting/>`_ deployments are the main entry points used to create new votes, vote, checking the status of a vote, and execute a successful vote.

.. csv-table::
   :header: "Vote Type", "Address"

   Ownership, `0xE478de485ad2fe566d49342Cbd03E49ed7DB3356 <https://etherscan.io/address/0xe478de485ad2fe566d49342cbd03e49ed7db3356>`_
   Parameter, `0xBCfF8B0b9419b9A88c44546519b1e909cF330399 <https://etherscan.io/address/0xbcff8b0b9419b9a88c44546519b1e909cf330399>`_
   Emergency, `0x1115c9b3168563354137cDc60efb66552dd50678 <https://etherscan.io/address/0x1115c9b3168563354137cdc60efb66552dd50678>`_

Agent
*****

Aragon `Agent <https://hack.aragon.org/docs/guides-use-agent>`_ deployments correspond to the different owner accounts within the DAO. Contract calls made as a result of a successful vote will execute from these addresses. When deploying new contracts, these addresses should be given appropriate access to admin functionality.

.. csv-table::
   :header: "Vote Type", "Address"

   Ownership, `0x40907540d8a6c65c637785e8f8b742ae6b0b9968 <https://etherscan.io/address/0x40907540d8a6c65c637785e8f8b742ae6b0b9968>`_
   Parameter, `0x4eeb3ba4f221ca16ed4a0cc7254e2e32df948c5f <https://etherscan.io/address/0x4eeb3ba4f221ca16ed4a0cc7254e2e32df948c5f>`_
   Emergency, `0x00669DF67E4827FCc0E48A1838a8d5AB79281909 <https://etherscan.io/address/0x00669DF67E4827FCc0E48A1838a8d5AB79281909>`_

Tokens
******

The following token addresses are used for determining voter weights within Curve's Aragon DAOs.

.. csv-table::
   :header: "Vote Type", "Address"

   Ownership / Parameter, `0x5f3b5DfEb7B28CDbD7FAba78963EE202a494e2A2 <https://etherscan.io/address/0x5f3b5DfEb7B28CDbD7FAba78963EE202a494e2A2>`_
   Emergency, `0x4c0947B16FB1f755A2D32EC21A0c4181f711C500 <https://etherscan.io/address/0x4c0947B16FB1f755A2D32EC21A0c4181f711C500>`_

Fee Burners
-----------

Burners are a fundamental component of the fee payout mechanism in Curve. A burner converts collected pool fees to an asset which can be converted to USDC. Ultimately, the exchanged for USDC is deposited to the 3Pool, as fees are paid out in 3CRV to veCRV holders. Depending on which tokens a pool contains, a specific burner implementation is used.

Here is a list of all burner contracts currently in use:

.. csv-table::
   :header: "Gauge", "Source", "Address"

   ABurner, `ABurner.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/burners/ABurner.vy>`_, `0x12220a63a2013133d54558c9d03c35288eac9b34 <https://etherscan.io/address/0x12220a63a2013133d54558c9d03c35288eac9b34#code>`_
   CryptoLPBurner, `CryptoLPBurner.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/burners/CryptoLPBurner.vy>`_, `0x0B5B9210d5015fD0c97FB19B32675b19703b0453 <https://etherscan.io/address/0x0B5B9210d5015fD0c97FB19B32675b19703b0453#code>`_
   CBurner, `CBurner.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/burners/CBurner.vy>`_, `0xdd0e10857d952c73b2fa39ce86308299df8774b8 <https://etherscan.io/address/0xdd0e10857d952c73b2fa39ce86308299df8774b8#code>`_
   LPBurner, `LPBurner.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/burners/LPBurner.vy>`_, `0xaa42C0CD9645A58dfeB699cCAeFBD30f19B1ff81 <https://etherscan.io/address/0xaa42C0CD9645A58dfeB699cCAeFBD30f19B1ff81#code>`_
   MetaBurner, `MetaBurner.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/burners/MetaBurner.vy>`_, `0xE4b65889469ad896e866331f0AB5652C1EcfB3E6 <https://etherscan.io/address/0xE4b65889469ad896e866331f0AB5652C1EcfB3E6#code>`_
   SynthBurner, `SynthBurner.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/burners/SynthBurner.vy>`_, `0x67a0213310202DBc2cbE788f4349B72fbA90f9Fa <https://etherscan.io/address/0x67a0213310202dbc2cbe788f4349b72fba90f9fa>`_
   USDNBurner, `USDNBurner.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/burners/USDNBurner.vy>`_, `0x06534b0BF7Ff378F162d4F348390BDA53b15fA35 <https://etherscan.io/address/0x06534b0BF7Ff378F162d4F348390BDA53b15fA35#code>`_
   UnderlyingBurner, `UnderlyingBurner.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/burners/UnderlyingBurner.vy>`_, `0x786b374b5eef874279f4b7b4de16940e57301a58 <https://etherscan.io/address/0x786b374b5eef874279f4b7b4de16940e57301a58#code>`_
   UniswapBurner, `UniswapBurner.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/burners/UniswapBurner.vy>`_, `0xf3b64840b39121b40d8685f1576b64c157ce2e24 <https://etherscan.io/address/0xf3b64840b39121b40d8685f1576b64c157ce2e24#code>`_
   YBurner, `YBurner.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/burners/YBurner.vy>`_, `0xd16ea3e5681234da84419512eb597362135cd8c9 <https://etherscan.io/address/0xd16ea3e5681234da84419512eb597362135cd8c9#code>`_

Pool Registry
=============

The pool registry serves as an on-chain information hub about the current state of Curve pools. For instance, on-chain integrators can fetch the current address of a Curve pool and query information about it.

Here is a list of all components of the pool registry currently in use:

.. csv-table::
   :header: "Name", "Source", "Address"

   Address Provider, `AddressProvider.vy <https://github.com/curvefi/curve-pool-registry/blob/master/contracts/AddressProvider.vy>`_, `0x0000000022d53366457f9d5e68ec105046fc4383 <https://etherscan.io/address/0x0000000022d53366457f9d5e68ec105046fc4383#code>`_
   Curve Calculator, `CurveCalc.vy <https://github.com/curvefi/curve-pool-registry/blob/master/contracts/CurveCalc.vy>`_, `0xc1DB00a8E5Ef7bfa476395cdbcc98235477cDE4E <https://etherscan.io/address/0xc1DB00a8E5Ef7bfa476395cdbcc98235477cDE4E#code>`_
   Pool Info, `PoolInfo.vy <https://github.com/curvefi/curve-pool-registry/blob/master/contracts/PoolInfo.vy>`_, `0xe64608E223433E8a03a1DaaeFD8Cb638C14B552C <https://etherscan.io/address/0xe64608E223433E8a03a1DaaeFD8Cb638C14B552C#code>`_
   Registry, `Registry.vy <https://github.com/curvefi/curve-pool-registry/blob/master/contracts/Registry.vy>`_, `0x90E00ACe148ca3b23Ac1bC8C240C2a7Dd9c2d7f5 <https://etherscan.io/address/0x90E00ACe148ca3b23Ac1bC8C240C2a7Dd9c2d7f5#code>`_

MetaPool Factory
================

The metapool factory allows for the permissionless deployment of Curve metapools. As discussed :ref:`here<factory-overview>`, the metapool factory has the following core components:

* The :ref:`factory<factory-deployer>` is the main contract used to deploy new metapools. It also acts a registry for finding the deployed pools and querying information about them.
* :ref:`Pools<factory-pools>` are deployed via a proxy contract. The implementation contract targetted by the proxy is determined according to the base pool. This is the same technique used to create pools in Uniswap V1.
* :ref:`Deposit contracts<factory-deposits>` ("zaps") are used for wrapping and unwrapping underlying assets when depositing into or withdrawing from pools.

.. csv-table::
   :header: "Name", "Source", "Address"

   Factory, `Factory.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/Factory.vy>`_, `0xB9fC157394Af804a3578134A6585C0dc9cc990d4 <https://etherscan.io/address/0xB9fC157394Af804a3578134A6585C0dc9cc990d4>`_
   Migrator, `PoolMigrator.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/PoolMigrator.vy>`_, `0xd6930b7f661257DA36F93160149b031735237594 <https://etherscan.io/address/0xd6930b7f661257DA36F93160149b031735237594>`_


Implementation Contracts
------------------------

The implementation contracts used for factory metapools are deployed to the mainnet at the following addresses:

.. csv-table::
   :header: "Name", "Source", "Address"

   3pool, `MetaImplementationUSD.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/MetaImplementationUSD.vy>`_, `0x5F890841f657d90E081bAbdB532A05996Af79Fe6 <https://etherscan.io/address/0x5F890841f657d90E081bAbdB532A05996Af79Fe6>`_
   sBTC, `MetaImplementationBTC.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/MetaImplementationBTC.vy>`_, `0x2f956eee002b0debd468cf2e0490d1aec65e027f <https://etherscan.io/address/0x2f956eee002b0debd468cf2e0490d1aec65e027f>`_


Deposit Zaps
------------

Deposit zaps for factory metapools are deployed to the mainnet at the following addresses:

.. csv-table::
   :header: "Name", "Source", "Address"

   3pool Deposit Zap, `DepositZapUSD.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/DepositZapUSD.vy>`_, `0xA79828DF1850E8a3A3064576f380D90aECDD3359 <https://etherscan.io/address/0xa79828df1850e8a3a3064576f380d90aecdd3359>`_
   sBTC Deposit Zap, `DepositZapBTC.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/DepositZapBTC.vy>`_, `0x7AbDBAf29929e7F8621B757D2a7c04d78d633834  <https://etherscan.io/address/0x7abdbaf29929e7f8621b757d2a7c04d78d633834>`_

Promoted Factory Pools
----------------------

Factory metapools which have been promoted to the flagship Curve UI.

.. csv-table::
   :header: "Pool", "Source", "Address"

   alUSD, `MetaImplementationUSD.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/MetaImplementationUSD.vy>`_, `0x43b4FdFD4Ff969587185cDB6f0BD875c5Fc83f8c <https://etherscan.io/address/0x43b4FdFD4Ff969587185cDB6f0BD875c5Fc83f8c#code>`_
   FRAX, `MetaImplementationUSD.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/MetaImplementationUSD.vy>`_, `0xd632f22692FaC7611d2AA1C0D552930D43CAEd3B <https://etherscan.io/address/0xd632f22692FaC7611d2AA1C0D552930D43CAEd3B#code>`_

Other Chains
============

Arbitrum
--------

Curve has several contracts deployed on `Arbitrum <https://offchainlabs.com/>`_. UI for these contracts is available at `arbitrum.curve.fi <https://arbitrum.curve.fi>`_.

Pools and Gauges
****************

.. csv-table::
   :header: "Name", "Source", "Address"

   2Pool, `StableSwap.vy <https://arbiscan.io/address/0x7f90122BF0700F9E7e1F688fe926940E8839F353#code>`_, `0x7f90122BF0700F9E7e1F688fe926940E8839F353 <https://arbiscan.io/address/0x7f90122BF0700F9E7e1F688fe926940E8839F353>`_
   2Pool LP Token, `StableSwap.vy <https://arbiscan.io/address/0x7f90122BF0700F9E7e1F688fe926940E8839F353#code>`_, `0x7f90122BF0700F9E7e1F688fe926940E8839F353 <https://arbiscan.io/address/0x7f90122BF0700F9E7e1F688fe926940E8839F353>`_
   2Pool Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0xCE5F24B7A95e9cBa7df4B54E911B4A3Dc8CDAf6f <https://arbiscan.io/address/0xCE5F24B7A95e9cBa7df4B54E911B4A3Dc8CDAf6f>`_
   2Pool Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0xCE5F24B7A95e9cBa7df4B54E911B4A3Dc8CDAf6f <https://etherscan.io/address/0xCE5F24B7A95e9cBa7df4B54E911B4A3Dc8CDAf6f>`_
   wBTC/renBTC Pool, `StableSwap.vy <https://arbiscan.io/address/0x3E01dD8a5E1fb3481F0F589056b428Fc308AF0Fb#code>`_, `0x3E01dD8a5E1fb3481F0F589056b428Fc308AF0Fb <https://arbiscan.io/address/0x3E01dD8a5E1fb3481F0F589056b428Fc308AF0Fb>`_
   wBTC/renBTC LP Token, `StableSwap.vy <https://arbiscan.io/address/0x3E01dD8a5E1fb3481F0F589056b428Fc308AF0Fb#code>`_, `0x3E01dD8a5E1fb3481F0F589056b428Fc308AF0Fb <https://arbiscan.io/address/0x3E01dD8a5E1fb3481F0F589056b428Fc308AF0Fb>`_
   wBTC/renBTC Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0xDB3fd1bfC67b5D4325cb31C04E0Cae52f1787FD6 <https://arbiscan.io/address/0xDB3fd1bfC67b5D4325cb31C04E0Cae52f1787FD6>`_
   wBTC/renBTC Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0xDB3fd1bfC67b5D4325cb31C04E0Cae52f1787FD6 <https://etherscan.io/address/0xDB3fd1bfC67b5D4325cb31C04E0Cae52f1787FD6>`_
   Tricrypto Pool, `CryptoSwap.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/deployment-logs/2021-09-13.%20Arbitrum/CryptoSwap.vy>`_, `0x960ea3e3C7FB317332d990873d354E18d7645590 <https://arbiscan.io/address/0x960ea3e3C7FB317332d990873d354E18d7645590>`_
   Tricrypto LP Token, `CurveTokenV5.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/contracts/CurveTokenV5.vy>`_, `0x8e0B8c8BB9db49a46697F3a5Bb8A308e744821D2 <https://arbiscan.io/address/0x8e0B8c8BB9db49a46697F3a5Bb8A308e744821D2>`_
   Tricrypto Zap, `CryptoZap.vy <https://arbiscan.io/address/0xF97c707024ef0DD3E77a0824555a46B622bfB500#code>`_, `0xF97c707024ef0DD3E77a0824555a46B622bfB500 <https://arbiscan.io/address/0xF97c707024ef0DD3E77a0824555a46B622bfB500>`_
   Tricrypto Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0x555766f3da968ecBefa690Ffd49A2Ac02f47aa5f <https://arbiscan.io/address/0x555766f3da968ecBefa690Ffd49A2Ac02f47aa5f>`_
   Tricrypto Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0x555766f3da968ecBefa690Ffd49A2Ac02f47aa5f <https://etherscan.io/address/0x555766f3da968ecBefa690Ffd49A2Ac02f47aa5f>`_
   EURs Pool, `CryptoSwap.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/deployment-logs/2021-10-30.%20EURS/CryptoSwap.vy>`_, `0xA827a652Ead76c6B0b3D19dba05452E06e25c27e <https://arbiscan.io/address/0xA827a652Ead76c6B0b3D19dba05452E06e25c27e>`_
   EURs LP Token, `CurveTokenV5.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/contracts/CurveTokenV5.vy>`_, `0x3dFe1324A0ee9d86337d06aEB829dEb4528DB9CA <https://arbiscan.io/address/0x3dFe1324A0ee9d86337d06aEB829dEb4528DB9CA>`_
   EURs Zap, `ZapTwoArbiEurs.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/deployment-logs/2021-10-30.%20EURS/ZapTwoArbiEurs.vy>`_, `0x25e2e8d104BC1A70492e2BE32dA7c1f8367F9d2c <https://arbiscan.io/address/0x25e2e8d104BC1A70492e2BE32dA7c1f8367F9d2c>`_
   EURs Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0x6339eF8Df0C2d3d3E7eE697E241666a916B81587 <https://arbiscan.io/address/0x6339eF8Df0C2d3d3E7eE697E241666a916B81587>`_
   EURs Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0x6339eF8Df0C2d3d3E7eE697E241666a916B81587 <https://etherscan.io/address/0x6339eF8Df0C2d3d3E7eE697E241666a916B81587>`_

Factories
*********

.. csv-table::
   :header: "Name", "Source", "Address"

   StableSwap Factory, `FactorySidechains.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/FactorySidechains.vy>`_, `0xb17b674D9c5CB2e441F8e196a2f048A81355d031 <https://arbiscan.io/address/0xb17b674D9c5CB2e441F8e196a2f048A81355d031>`_
   MetaUSD Zap, `MetaUSDZap.vy <https://arbiscan.io/address/0x7544Fe3d184b6B55D6B36c3FCA1157eE0Ba30287#code>`_, `0x7544Fe3d184b6B55D6B36c3FCA1157eE0Ba30287 <https://arbiscan.io/address/0x7544Fe3d184b6B55D6B36c3FCA1157eE0Ba30287>`_
   MetaBTC Zap, `MetaBTCZap.vy <https://arbiscan.io/address/0x803A2B40c5a9BB2B86DD630B274Fa2A9202874C2#code>`_, `0x803A2B40c5a9BB2B86DD630B274Fa2A9202874C2 <https://arbiscan.io/address/0x803A2B40c5a9BB2B86DD630B274Fa2A9202874C2>`_
   X-Chain Gauge Factory, `ChildGaugeFactory.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/ChildGaugeFactory.vy>`_, `0xabC000d88f23Bb45525E447528DBF656A9D55bf5 <https://arbiscan.io/address/0xabC000d88f23Bb45525E447528DBF656A9D55bf5>`_


Aurora
------

Curve has several contracts deployed on `Aurora <https://aurora.dev/start/>`_. UI for these contracts is available at `aurora.curve.fi <https://aurora.curve.fi>`_.

Pools and Gauges
****************

.. csv-table::
   :header: "Name", "Source", "Address"

   3Pool, `StableSwap.vy <https://aurorascan.dev/address/0xbF7E49483881C76487b0989CD7d9A8239B20CA41#code>`_, `0xbF7E49483881C76487b0989CD7d9A8239B20CA41 <https://aurorascan.dev/address/0xbF7E49483881C76487b0989CD7d9A8239B20CA41>`_
   3Pool LP Token, `StableSwap.vy <https://aurorascan.dev/address/0xbF7E49483881C76487b0989CD7d9A8239B20CA41#code>`_, `0xbF7E49483881C76487b0989CD7d9A8239B20CA41 <https://aurorascan.dev/address/0xbF7E49483881C76487b0989CD7d9A8239B20CA41>`_
   3Pool Rewards-only Gauge, `RewardsOnlyGauge.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/RewardsOnlyGauge.vy>`_, `0xC2b1DF84112619D190193E48148000e3990Bf627 <https://aurorascan.dev/address/0xc2b1df84112619d190193e48148000e3990bf627>`_

Avalanche
---------

Curve has several contracts deployed on `Avalanche <https://www.avax.network/>`_. UI for these contracts is available at `avax.curve.fi <https://avax.curve.fi>`_.

Pools and Gauges
****************

.. csv-table::
   :header: "Name", "Source", "Address"

   Aave Pool, `StableSwap.vy <https://snowtrace.io/address/0x7f90122BF0700F9E7e1F688fe926940E8839F353#code>`_, `0x7f90122BF0700F9E7e1F688fe926940E8839F353 <https://snowtrace.io/address/0x7f90122BF0700F9E7e1F688fe926940E8839F353>`_
   Aave LP Token, `CurveToken.vy <https://snowtrace.io/address/0x1337BedC9D22ecbe766dF105c9623922A27963EC#code>`_, `0x1337BedC9D22ecbe766dF105c9623922A27963EC <https://snowtrace.io/address/0x1337BedC9D22ecbe766dF105c9623922A27963EC>`_
   Aave Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0x4620D46b4db7fB04a01A75fFed228Bc027C9A899 <https://snowtrace.io/address/0x4620D46b4db7fB04a01A75fFed228Bc027C9A899>`_
   Aave Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0x4620D46b4db7fB04a01A75fFed228Bc027C9A899 <https://etherscan.io/address/0x4620D46b4db7fB04a01A75fFed228Bc027C9A899>`_
   renBTC Pool, `StableSwap.vy <https://snowtrace.io/address/0x16a7DA911A4DD1d83F3fF066fE28F3C792C50d90>`_, `0xC2b1DF84112619D190193E48148000e3990Bf627 <https://snowtrace.io/address/0xC2b1DF84112619D190193E48148000e3990Bf627>`_
   renBTC LP Token, `StableSwap.vy <https://snowtrace.io/address/0x16a7DA911A4DD1d83F3fF066fE28F3C792C50d90>`_, `0xC2b1DF84112619D190193E48148000e3990Bf627 <https://snowtrace.io/address/0xC2b1DF84112619D190193E48148000e3990Bf627>`_
   renBTC Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0x00F7d467ef51E44f11f52a0c0Bef2E56C271b264 <https://snowtrace.io/address/0x00F7d467ef51E44f11f52a0c0Bef2E56C271b264>`_
   renBTC Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0x00F7d467ef51E44f11f52a0c0Bef2E56C271b264 <https://etherscan.io/address/0x00F7d467ef51E44f11f52a0c0Bef2E56C271b264>`_
   ATriCrypto Pool, `CryptoSwap.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/deployment-logs/2021-10-04.%20Avax/CryptoSwap.vy>`_, `0xB755B949C126C04e0348DD881a5cF55d424742B2 <https://snowtrace.io/address/0xB755B949C126C04e0348DD881a5cF55d424742B2>`_
   ATriCrypto LP Token, `CurveToken.vy <https://snowtrace.io/address/0x1daB6560494B04473A0BE3E7D83CF3Fdf3a51828#code>`_, `0x1daB6560494B04473A0BE3E7D83CF3Fdf3a51828 <https://snowtrace.io/address/0x1daB6560494B04473A0BE3E7D83CF3Fdf3a51828>`_
   ATriCrypto Zap, `CryptoZap.vy <https://snowtrace.io/address/0x58e57cA18B7A47112b877E31929798Cd3D703b0f#code>`_, `0x58e57cA18B7A47112b877E31929798Cd3D703b0f <https://snowtrace.io/address/0x58e57cA18B7A47112b877E31929798Cd3D703b0f>`_
   ATriCrypto Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0x1879075f1c055564CB968905aC404A5A01a1699A <https://snowtrace.io/address/0x1879075f1c055564CB968905aC404A5A01a1699A>`_
   ATriCrypto Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0x1879075f1c055564CB968905aC404A5A01a1699A <https://etherscan.io/address/0x1879075f1c055564CB968905aC404A5A01a1699A>`_

Factories
*********

.. csv-table::
   :header: "Name", "Source", "Address"

   StableSwap Factory, `FactorySidechains.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/FactorySidechains.vy>`_, `0xb17b674D9c5CB2e441F8e196a2f048A81355d031 <https://snowtrace.io/address/0xb17b674D9c5CB2e441F8e196a2f048A81355d031>`_
   MetaUSD Zap, `MetaUSDZap.vy <https://snowtrace.io/address/0x001E3BA199B4FF4B5B6e97aCD96daFC0E2e4156e#code>`_, `0x001E3BA199B4FF4B5B6e97aCD96daFC0E2e4156e <https://snowtrace.io/address/0x001E3BA199B4FF4B5B6e97aCD96daFC0E2e4156e>`_
   MetaBTC Zap, `MetaBTCZap.vy <https://snowtrace.io/address/0xEeB3DDBcc4174e0b3fd1C13aD462b95D11Ef42C3#code>`_, `0xEeB3DDBcc4174e0b3fd1C13aD462b95D11Ef42C3 <https://snowtrace.io/address/0xEeB3DDBcc4174e0b3fd1C13aD462b95D11Ef42C3>`_
   X-Chain Gauge Factory, `ChildGaugeFactory.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/ChildGaugeFactory.vy>`_, `0xabC000d88f23Bb45525E447528DBF656A9D55bf5 <https://snowtrace.io/address/0xabC000d88f23Bb45525E447528DBF656A9D55bf5>`_


Fantom
-------

Curve has several contracts deployed on `Fantom <https://fantom.foundation/>`_. UI for these contracts is available at `ftm.curve.fi <https://ftm.curve.fi>`_.

Pools and Gauges
****************

.. csv-table::
   :header: "Name", "Source", "Address"

   2Pool Pool, `StableSwap2Pool.vy <https://github.com/curvefi/curve-contract-fantom/blob/master/contracts/pools/2pool/StableSwap2Pool.vy>`_, `0x27E611FD27b276ACbd5Ffd632E5eAEBEC9761E40 <https://ftmscan.com/address/0x27E611FD27b276ACbd5Ffd632E5eAEBEC9761E40>`_
   2Pool LP Token, `StableSwap2Pool.vy <https://github.com/curvefi/curve-contract-fantom/blob/master/contracts/pools/2pool/StableSwap2Pool.vy>`_, `0x27E611FD27b276ACbd5Ffd632E5eAEBEC9761E40 <https://ftmscan.com/address/0x27E611FD27b276ACbd5Ffd632E5eAEBEC9761E40>`_
   2Pool Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0x15bB164F9827De760174d3d3dAD6816eF50dE13c <https://ftmscan.com/address/0x15bB164F9827De760174d3d3dAD6816eF50dE13c>`_
   2Pool Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0x15bB164F9827De760174d3d3dAD6816eF50dE13c <https://etherscan.io/address/0x15bB164F9827De760174d3d3dAD6816eF50dE13c>`_
   fUSDT Pool, `StableSwapFUSDT.vy <https://github.com/curvefi/curve-contract-fantom/blob/master/contracts/pools/fusdt/StableSwapFUSDT.vy>`_, `0x92D5ebF3593a92888C25C0AbEF126583d4b5312E <https://ftmscan.com/address/0x92D5ebF3593a92888C25C0AbEF126583d4b5312E>`_
   fUSDT LP Token, `StableSwap2Pool.vy <https://github.com/curvefi/curve-contract-fantom/blob/master/contracts/pools/2pool/StableSwap2Pool.vy>`_, `0x92D5ebF3593a92888C25C0AbEF126583d4b5312E <https://ftmscan.com/address/0x92D5ebF3593a92888C25C0AbEF126583d4b5312E>`_
   fUSDT Root Chain Gauge, `RootGaugeAnyswap.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/sidechain/RootGaugeAnyswap.vy>`_, `0xfE1A3dD8b169fB5BF0D5dbFe813d956F39fF6310 <https://etherscan.io/address/0xfE1A3dD8b169fB5BF0D5dbFe813d956F39fF6310>`_
   fUSDT Child Chain Streamer, `ChildChainStreamer.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/streamers/ChildChainStreamer.vy>`_, `0xfE1A3dD8b169fB5BF0D5dbFe813d956F39fF6310 <https://ftmscan.com/address/0xfE1A3dD8b169fB5BF0D5dbFe813d956F39fF6310>`_
   fUSDT Gauge, `RewardsOnlyGauge.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/RewardsOnlyGauge.vy>`_, `0x06e3C4da96fd076b97b7ca3Ae23527314b6140dF <https://ftmscan.com/address/0x06e3C4da96fd076b97b7ca3Ae23527314b6140dF>`_
   renBTC Pool, `StableSwapREN.vy <https://github.com/skellet0r/curve-contract-fantom/blob/master/contracts/pools/ren/StableSwapREN.vy>`_, `0x3eF6A01A0f81D6046290f3e2A8c5b843e738E604 <https://ftmscan.com/address/0x3eF6A01A0f81D6046290f3e2A8c5b843e738E604>`_
   renBTC LP Token, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract-fantom/blob/master/contracts/CurveTokenV3.vy>`_, `0x5B5CFE992AdAC0C9D48E05854B2d91C73a003858 <https://ftmscan.com/address/0x5B5CFE992AdAC0C9D48E05854B2d91C73a003858>`_
   renBTC Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0xbC38bD19227F91424eD4132F630f51C9A42Fa338 <https://ftmscan.com/address/0xbC38bD19227F91424eD4132F630f51C9A42Fa338>`_
   renBTC Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0xbC38bD19227F91424eD4132F630f51C9A42Fa338 <https://etherscan.io/address/0xbC38bD19227F91424eD4132F630f51C9A42Fa338>`_
   Geist Pool, `StableSwap.vy <https://ftmscan.com/address/0x0fa949783947Bf6c1b171DB13AEACBB488845B3f#code>`_, `0x0fa949783947Bf6c1b171DB13AEACBB488845B3f <https://ftmscan.com/address/0x0fa949783947Bf6c1b171DB13AEACBB488845B3f>`_
   Geist LP Token, `CurveToken.vy <https://ftmscan.com/address/0xD02a30d33153877BC20e5721ee53DeDEE0422B2F#code>`_, `0xD02a30d33153877BC20e5721ee53DeDEE0422B2F <https://ftmscan.com/address/0xD02a30d33153877BC20e5721ee53DeDEE0422B2F>`_
   Geist Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0xF7b9c402c4D6c2eDbA04a7a515b53D11B1E9b2cc <https://ftmscan.com/address/0xF7b9c402c4D6c2eDbA04a7a515b53D11B1E9b2cc>`_
   Geist Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0xF7b9c402c4D6c2eDbA04a7a515b53D11B1E9b2cc <https://etherscan.io/address/0xF7b9c402c4D6c2eDbA04a7a515b53D11B1E9b2cc>`_
   TriCrypto Pool, `CryptoSwap.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/deployment-logs/2021-09-17.%20Fantom/CryptoSwap.vy>`_, `0x3a1659Ddcf2339Be3aeA159cA010979FB49155FF <https://ftmscan.com/address/0x3a1659Ddcf2339Be3aeA159cA010979FB49155FF>`_
   TriCrypto LP Token, `CurveToken.vy <https://ftmscan.com/address/0x58e57cA18B7A47112b877E31929798Cd3D703b0f#code>`_, `0x58e57cA18B7A47112b877E31929798Cd3D703b0f <https://ftmscan.com/address/0x58e57cA18B7A47112b877E31929798Cd3D703b0f>`_
   TriCrypto Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0x319E268f0A4C85D404734ee7958857F5891506d7 <https://ftmscan.com/address/0x319E268f0A4C85D404734ee7958857F5891506d7>`_
   TriCrypto Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0x319E268f0A4C85D404734ee7958857F5891506d7 <https://etherscan.io/address/0x319E268f0A4C85D404734ee7958857F5891506d7>`_
   IronBank Pool, `StableSwap.vy <https://ftmscan.com/address/0x4FC8D635c3cB1d0aa123859e2B2587d0FF2707b1#code>`_, `0x4FC8D635c3cB1d0aa123859e2B2587d0FF2707b1 <https://ftmscan.com/address/0x4FC8D635c3cB1d0aa123859e2B2587d0FF2707b1>`_
   IronBank LP Token, `CurveToken.vy <https://ftmscan.com/address/0xDf38ec60c0eC001142a33eAa039e49E9b84E64ED#code>`_, `0xDf38ec60c0eC001142a33eAa039e49E9b84E64ED <https://ftmscan.com/address/0xDf38ec60c0eC001142a33eAa039e49E9b84E64ED>`_
   IronBank Rewards-only Gauge, `RewardsOnlyGauge.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/RewardsOnlyGauge.vy>`_, `0xDee85272EAe1aB4afBc6433F4d819BaBC9c7045A <https://ftmscan.com/address/0xdee85272eae1ab4afbc6433f4d819babc9c7045a>`_

Factories
*********

.. csv-table::
   :header: "Name", "Source", "Address"

   StableSwap Factory, `FactorySidechains.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/FactorySidechains.vy>`_, `0x686d67265703d1f124c45e33d47d794c566889ba <https://ftmscan.com/address/0x686d67265703d1f124c45e33d47d794c566889ba>`_
   MetaUSD Zap (2pool), `MetaUSDZap.vy <https://ftmscan.com/address/0x78D51EB71a62c081550EfcC0a9F9Ea94B2Ef081c#code>`_, `0x78D51EB71a62c081550EfcC0a9F9Ea94B2Ef081c <https://ftmscan.com/address/0x78D51EB71a62c081550EfcC0a9F9Ea94B2Ef081c>`_
   MetaUSD Zap (geist), `MetaUSDZap.vy <https://ftmscan.com/address/0x247aEB220E87f24c40C9F86b65d6bd5d3c987B55#code>`_, `0x247aEB220E87f24c40C9F86b65d6bd5d3c987B55 <https://ftmscan.com/address/0x247aEB220E87f24c40C9F86b65d6bd5d3c987B55>`_
   MetaBTC Zap, `MetaBTCZap.vy <https://ftmscan.com/address/0x001E3BA199B4FF4B5B6e97aCD96daFC0E2e4156e#code>`_, `0x001E3BA199B4FF4B5B6e97aCD96daFC0E2e4156e <https://ftmscan.com/address/0x001E3BA199B4FF4B5B6e97aCD96daFC0E2e4156e>`_
   X-Chain Gauge Factory, `ChildGaugeFactory.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/ChildGaugeFactory.vy>`_, `0xabC000d88f23Bb45525E447528DBF656A9D55bf5 <https://ftmscan.com/address/0xabC000d88f23Bb45525E447528DBF656A9D55bf5>`_


Harmony
-------

Curve has several contracts deployed on `Harmony <https://www.harmony.one/>`_. UI for these contracts is available at `harmony.curve.fi <https://harmony.curve.fi>`_.

Pools and Gauges
****************

.. csv-table::
   :header: "Name", "Source", "Address"

   3Pool, `StableSwap.vy <https://explorer.harmony.one/address/0xc5cfada84e902ad92dd40194f0883ad49639b023>`_, `0xC5cfaDA84E902aD92DD40194f0883ad49639b023 <https://explorer.harmony.one/address/0xc5cfada84e902ad92dd40194f0883ad49639b023>`_
   3Pool LP Token, `StableSwap.vy <https://explorer.harmony.one/address/0xc5cfada84e902ad92dd40194f0883ad49639b023>`_, `0xC5cfaDA84E902aD92DD40194f0883ad49639b023 <https://explorer.harmony.one/address/0xc5cfada84e902ad92dd40194f0883ad49639b023>`_
   3Pool RewardsOnly Gauge, `RewardsOnlyGauge.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/RewardsOnlyGauge.vy>`_, `0xbF7E49483881C76487b0989CD7d9A8239B20CA41 <https://explorer.harmony.one/address/0xbF7E49483881C76487b0989CD7d9A8239B20CA41>`_
   TriCrypto, `CryptoSwap.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/deployment-logs/2021-10-17.%20Hamony/CryptoSwap.vy>`_, `0x0e3Dc2BcbFEa84072A0c794B7653d3db364154e0 <https://explorer.harmony.one/address/0xc5cfada84e902ad92dd40194f0883ad49639b023>`_
   TriCrypto LP Token, `Token.json <https://github.com/curvefi/curve-crypto-contract/blob/master/deployment-logs/2021-10-17.%20Hamony/swap.json>`_, `0xC5cfaDA84E902aD92DD40194f0883ad49639b023 <https://explorer.harmony.one/address/0x99E8eD28B97c7F1878776eD94fFC77CABFB9B726>`_
   TriCrypto Zap, `ZapHarmony.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/deployment-logs/2021-10-17.%20Hamony/ZapHarmony.vy>`_, `0x76147c0C989670D106b57763a24410A2a22e335E <https://explorer.harmony.one/address/0x76147c0c989670d106b57763a24410a2a22e335e>`_
   TriCrypto Gauge, `RewardsOnlyGauge.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/RewardsOnlyGauge.vy>`_, `0xF98450B5602fa59CC66e1379DFfB6FDDc724CfC4 <https://explorer.harmony.one/address/0xF98450B5602fa59CC66e1379DFfB6FDDc724CfC4>`_


Moonbeam
--------

Curve has several contracts deployed on `Moonbeam <https://moonbeam.network/>`_. UI for these contracts is available at `moonbeam.curve.fi <https://harmony.curve.fi>`_.

Pools
*****

.. csv-table::
   :header: "Name", "Source", "Address"

   3Pool, `StableSwap.vy <https://moonscan.io/address/0xace58a26b8db90498ef0330fdc9c2655db0c45e2#code>`_, `0xace58a26b8Db90498eF0330fDC9C2655db0C45E2 <https://moonscan.io/address/0xace58a26b8db90498ef0330fdc9c2655db0c45e2>`_
   3Pool LP Token, `StableSwap.vy <https://moonscan.io/address/0xace58a26b8db90498ef0330fdc9c2655db0c45e2#code>`_, `0xace58a26b8Db90498eF0330fDC9C2655db0C45E2 <https://moonscan.io/address/0xace58a26b8db90498ef0330fdc9c2655db0c45e2>`_

Factories
*********

.. csv-table::
   :header: "Name", "Source", "Address"

   StableSwap Factory, `FactorySidechains.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/FactorySidechains.vy>`_, `0x4244eB811D6e0Ef302326675207A95113dB4E1F8 <https://moonscan.io/address/0x4244eB811D6e0Ef302326675207A95113dB4E1F8>`_
   X-Chain Gauge Factory, `ChildGaugeFactory.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/ChildGaugeFactory.vy>`_, `0xabC000d88f23Bb45525E447528DBF656A9D55bf5 <https://moonscan.io/address/0xabC000d88f23Bb45525E447528DBF656A9D55bf5>`_


Optimism
--------

Curve has several contracts deployed on `Optimism <https://www.optimism.io/>`_. UI for these contracts is available at `optimism.curve.fi <https://optimism.curve.fi>`_.

Pools
*****

.. csv-table::
   :header: "Name", "Source", "Address"

    3pool, `StableSwap.vy <https://optimistic.etherscan.io/address/0x1337BedC9D22ecbe766dF105c9623922A27963EC#code>`_, `0x1337BedC9D22ecbe766dF105c9623922A27963ECA <https://optimistic.etherscan.io/address/0x1337BedC9D22ecbe766dF105c9623922A27963EC>`_
    3pool LP Token, `StableSwap.vy <https://optimistic.etherscan.io/address/0x1337BedC9D22ecbe766dF105c9623922A27963EC#code>`_, `0x1337BedC9D22ecbe766dF105c9623922A27963ECA <https://optimistic.etherscan.io/address/0x1337BedC9D22ecbe766dF105c9623922A27963EC>`_
    3Pool Rewards Only Gauge, `RewardsOnlyGauge.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/RewardsOnlyGauge.vy>`_, `0x7f90122BF0700F9E7e1F688fe926940E8839F353 <https://optimistic.etherscan.io/address/0x7f90122bf0700f9e7e1f688fe926940e8839f353#code>`_


Factories
*********

.. csv-table::
   :header: "Name", "Source", "Address"

   StableSwap Factory, `FactorySidechains.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/FactorySidechains.vy>`_, `0x2db0E83599a91b508Ac268a6197b8B14F5e72840 <https://optimistic.etherscan.io/address/0x2db0E83599a91b508Ac268a6197b8B14F5e72840>`_
   X-Chain Gauge Factory, `ChildGaugeFactory.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/ChildGaugeFactory.vy>`_, `0xabC000d88f23Bb45525E447528DBF656A9D55bf5 <https://optimistic.etherscan.io/address/0xabC000d88f23Bb45525E447528DBF656A9D55bf5>`_


Polygon
-------

Curve has several contracts deployed on `Polygon <https://polygon.technology/>`_. UI for these contracts is available at `polygon.curve.fi <https://polygon.curve.fi>`_.

Pools and Gauges
****************

.. csv-table::
   :header: "Name", "Source", "Address"

   ATriCrypto Pool, `CurveCryptoSwapMatic.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/contracts/matic/CurveCryptoSwapMatic.vy>`_, `0x751B1e21756bDbc307CBcC5085c042a0e9AaEf36 <https://polygonscan.com/address/0x751B1e21756bDbc307CBcC5085c042a0e9AaEf36>`_
   ATriCrypto Zap, `ZapAave.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/contracts/matic/ZapAave.vy>`_, `0x3FCD5De6A9fC8A99995c406c77DDa3eD7E406f81 <https://polygonscan.com/address/0x3FCD5De6A9fC8A99995c406c77DDa3eD7E406f81>`_
   ATriCrypto LP Token, `CurveTokenV4.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/contracts/CurveTokenV4.vy>`_, `0x8096ac61db23291252574D49f036f0f9ed8ab390 <https://polygonscan.com/address/0x8096ac61db23291252574D49f036f0f9ed8ab390>`_
   ATriCrypto Root Chain Gauge, `RootGaugePolygon.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/sidechain/RootGaugePolygon.vy>`_, `0x060e386eCfBacf42Aa72171Af9EFe17b3993fC4F <https://etherscan.io/address/0x060e386eCfBacf42Aa72171Af9EFe17b3993fC4F>`_
   ATriCrypto Child Chain Streamer, `ChildChainStreamer.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/streamers/ChildChainStreamer.vy>`_, `0x060e386eCfBacf42Aa72171Af9EFe17b3993fC4F <https://polygonscan.com/address/0x060e386eCfBacf42Aa72171Af9EFe17b3993fC4F>`_
   ATriCrypto Reward Claimer, `RewardClaimer.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/streamers/RewardClaimer.vy>`_, `0xe84AE0321f88349B5F1119464EEB242b7De51a69 <https://polygonscan.com/address/0xe84AE0321f88349B5F1119464EEB242b7De51a69>`_
   ATriCrypto Gauge, `RewardsOnlyGauge.vy <https://github.com/curvefi/curve-dao-contracts/blob/master/contracts/gauges/RewardsOnlyGauge.vy>`_, `0xb0a366b987d77b5eD5803cBd95C80bB6DEaB48C0 <https://polygonscan.com/address/0xb0a366b987d77b5eD5803cBd95C80bB6DEaB48C0>`_
   ATriCrypto3 Pool, `CryptoSwap.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/deployment-logs/2021-08-27.%20Polygon%20redeployment/CryptoSwap.vy>`_, `0x92215849c439E1f8612b6646060B4E3E5ef822cC <https://polygonscan.com/address/0x92215849c439E1f8612b6646060B4E3E5ef822cC>`_
   ATriCrypto3 LP Token, `CurveTokenV5.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/contracts/CurveTokenV5.vy>`_, `0xdAD97F7713Ae9437fa9249920eC8507e5FbB23d3 <https://polygonscan.com/address/0xdAD97F7713Ae9437fa9249920eC8507e5FbB23d3>`_
   ATriCrypto3 Zap, `CryptoZap.vy <https://polygonscan.com/address/0x1d8b86e3D88cDb2d34688e87E72F388Cb541B7C8#code>`_, `0x1d8b86e3D88cDb2d34688e87E72F388Cb541B7C8 <https://polygonscan.com/address/0x1d8b86e3D88cDb2d34688e87E72F388Cb541B7C8>`_
   ATriCrypto3 Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0xBb1B19495B8FE7C402427479B9aC14886cbbaaeE <https://polygonscan.com/address/0xBb1B19495B8FE7C402427479B9aC14886cbbaaeE>`_
   ATriCrypto3 Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0xBb1B19495B8FE7C402427479B9aC14886cbbaaeE <https://etherscan.io/address/0xBb1B19495B8FE7C402427479B9aC14886cbbaaeE>`_
   Aave Pool, `StableSwapAave.vy <https://github.com/curvefi/curve-contract-polygon/blob/master/contracts/pools/aave/StableSwapAave.vy>`_, `0x445FE580eF8d70FF569aB36e80c647af338db351 <https://polygonscan.com/address/0x445FE580eF8d70FF569aB36e80c647af338db351>`_
   Aave LP Token, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract-polygon/blob/master/contracts/CurveTokenV3.vy>`_, `0xE7a24EF0C5e95Ffb0f6684b813A78F2a3AD7D171 <https://polygonscan.com/address/0xE7a24EF0C5e95Ffb0f6684b813A78F2a3AD7D171>`_
   Aave Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0x20759F567BB3EcDB55c817c9a1d13076aB215EdC <https://polygonscan.com/address/0x20759F567BB3EcDB55c817c9a1d13076aB215EdC>`_
   Aave Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0x20759F567BB3EcDB55c817c9a1d13076aB215EdC <https://etherscan.io/address/0x20759F567BB3EcDB55c817c9a1d13076aB215EdC>`_
   renBTC Pool, `StableSwapREN.vy <https://github.com/curvefi/curve-contract-polygon/blob/master/contracts/pools/ren/StableSwapREN.vy>`_, `0xC2d95EEF97Ec6C17551d45e77B590dc1F9117C67 <https://polygonscan.com/address/0xC2d95EEF97Ec6C17551d45e77B590dc1F9117C67>`_
   renBTC LP Token, `CurveTokenV3.vy <https://github.com/curvefi/curve-contract-polygon/blob/master/contracts/CurveTokenV3.vy>`_, `0xf8a57c1d3b9629b77b6726a042ca48990A84Fb49 <https://polygonscan.com/address/0xf8a57c1d3b9629b77b6726a042ca48990A84Fb49>`_
   renBTC Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0x8D9649e50A0d1da8E939f800fB926cdE8f18B47D <https://polygonscan.com/address/0x8D9649e50A0d1da8E939f800fB926cdE8f18B47D>`_
   renBTC Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0x8D9649e50A0d1da8E939f800fB926cdE8f18B47D <https://etherscan.io/address/0x8D9649e50A0d1da8E939f800fB926cdE8f18B47D>`_
   EURTUSD Pool, `CryptoSwap.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/deployment-logs/2021-10-30.%20EURT/CryptoSwap.vy>`_, `0xB446BF7b8D6D4276d0c75eC0e3ee8dD7Fe15783A <https://polygonscan.com/address/0xB446BF7b8D6D4276d0c75eC0e3ee8dD7Fe15783A>`_
   EURTUSD LP Token, `CurveToken.vy <https://polygonscan.com/address/0x600743B1d8A96438bD46836fD34977a00293f6Aa#code>`_, `0x600743B1d8A96438bD46836fD34977a00293f6Aa <https://polygonscan.com/address/0x600743B1d8A96438bD46836fD34977a00293f6Aa>`_
   EURTUSD Zap, `CryptoZap.vy <https://polygonscan.com/address/0x225FB4176f0E20CDb66b4a3DF70CA3063281E855#code>`_, `0x225FB4176f0E20CDb66b4a3DF70CA3063281E855 <https://polygonscan.com/address/0x225FB4176f0E20CDb66b4a3DF70CA3063281E855>`_
   EURTUSD Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0x8b397084699Cc64E429F610F81Fac13bf061ef55 <https://polygonscan.com/address/0x8b397084699Cc64E429F610F81Fac13bf061ef55>`_
   EURTUSD Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0x8b397084699Cc64E429F610F81Fac13bf061ef55 <https://etherscan.io/address/0x8b397084699Cc64E429F610F81Fac13bf061ef55>`_
   EURs Pool, `CryptoSwap.vy <https://github.com/curvefi/curve-crypto-contract/blob/master/deployment-logs/2022-03-09.%20EURS-polygon/CryptoSwap.vy>`_, `0x9b3d675FDbe6a0935E8B7d1941bc6f78253549B7 <https://polygonscan.com/address/0x9b3d675FDbe6a0935E8B7d1941bc6f78253549B7>`_
   EURs LP Token, `Token.json <https://github.com/curvefi/curve-crypto-contract/blob/master/deployment-logs/2022-03-09.%20EURS-polygon/token.json>`_, `0x7BD9757FbAc089d60DaFF1Fa6bfE3BC99b0F5735 <https://polygonscan.com/address/0x7BD9757FbAc089d60DaFF1Fa6bfE3BC99b0F5735>`_
   EURs Zap, `Zap.json <https://github.com/curvefi/curve-crypto-contract/blob/master/deployment-logs/2022-03-09.%20EURS-polygon/zap.json>`_, `0x4DF7eF55E99a56851187822d96B4E17D98A47DeD <https://polygonscan.com/address/0x4DF7eF55E99a56851187822d96B4E17D98A47DeD>`_


Rewards and Admin Fees
**********************

.. csv-table::
   :header: "Name", "Source", "Address"

   WMATIC Distributor, `RewardStream.vy <https://github.com/curvefi/curve-contract-polygon/blob/master/contracts/gauges/RewardStream.vy>`_, `0xBdFF0C27dd073C119ebcb1299a68A6A92aE607F0 <https://polygonscan.com/address/0xBdFF0C27dd073C119ebcb1299a68A6A92aE607F0>`_
   ABurner, `ABurner.vy <https://github.com/curvefi/curve-contract-polygon/blob/master/contracts/burners/ABurner.vy>`_, `0xA237034249290De2B07988Ac64b96f22c0E76fE0 <https://polygonscan.com/address/0xA237034249290De2B07988Ac64b96f22c0E76fE0>`_
   Admin Fee Bridge (Polygon), `ChildBurner.vy <https://github.com/curvefi/curve-contract-polygon/blob/master/contracts/bridge/ChildBurner.vy>`_, `0x4473243A61b5193670D1324872368d015081822f <https://polygonscan.com/address/0x4473243A61b5193670D1324872368d015081822f>`_
   Admin Fee Bridge (Ethereum), `RootForwarder.vy <https://github.com/curvefi/curve-contract-polygon/blob/master/contracts/bridge/RootForwarder.vy>`_, `0x4473243A61b5193670D1324872368d015081822f <https://etherscan.io/address/0x4473243A61b5193670D1324872368d015081822f>`_

Factories
*********

.. csv-table::
   :header: "Name", "Source", "Address"

   StableSwap Factory, `FactorySidechains.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/FactorySidechains.vy>`_, `0x722272d36ef0da72ff51c5a65db7b870e2e8d4ee <https://polygonscan.com/address/0x722272d36ef0da72ff51c5a65db7b870e2e8d4ee>`_
   MetaUSD Zap, `MetaUSDZap.vy <https://polygonscan.com/address/0x5ab5C56B9db92Ba45a0B46a207286cD83C15C939#code>`_, `0x5ab5C56B9db92Ba45a0B46a207286cD83C15C939 <https://polygonscan.com/address/0x5ab5C56B9db92Ba45a0B46a207286cD83C15C939>`_
   MetaBTC Zap, `MetaBTCZap.vy <https://polygonscan.com/address/0xE2e6DC1708337A6e59f227921db08F21e3394723#code>`_, `0xE2e6DC1708337A6e59f227921db08F21e3394723 <https://polygonscan.com/address/0xE2e6DC1708337A6e59f227921db08F21e3394723>`_
   X-Chain Gauge Factory, `ChildGaugeFactory.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/ChildGaugeFactory.vy>`_, `0xabC000d88f23Bb45525E447528DBF656A9D55bf5 <https://polygonscan.com/address/0xabC000d88f23Bb45525E447528DBF656A9D55bf5>`_


XDai
----

Curve has several contracts deployed on `XDai <https://www.xdaichain.com//>`_. UI for these contracts is available at `xdai.curve.fi <https://xdai.curve.fi>`_.

Pools and Gauges
****************

.. csv-table::
   :header: "Name", "Source", "Address"

   x3Pool Pool, `StableSwap3Pool.vy <https://github.com/curvefi/curve-contract-xdai/blob/master/contracts/pools/2pool/StableSwap3Pool.vy>`_, `0x7f90122BF0700F9E7e1F688fe926940E8839F353 <https://blockscout.com/xdai/mainnet/address/0x7f90122BF0700F9E7e1F688fe926940E8839F353>`_
   x3Pool LP Token, `StableSwap3Pool.vy <https://github.com/curvefi/curve-contract-xdai/blob/master/contracts/pools/2pool/StableSwap3Pool.vy>`_, `0x1337BedC9D22ecbe766dF105c9623922A27963EC <https://blockscout.com/xdai/mainnet/address/0x6C09F6727113543Fd061a721da512B7eFCDD0267>`_
   x3Pool Child Gauge, `ChildGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/ChildGauge.vy>`_, `0xB721Cc32160Ab0da2614CC6aB16eD822Aeebc101 <https://blockscout.com/xdai/mainnet/address/0xB721Cc32160Ab0da2614CC6aB16eD822Aeebc101>`_
   x3Pool Root Gauge, `RootGauge.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/implementations/RootGauge.vy>`_, `0xB721Cc32160Ab0da2614CC6aB16eD822Aeebc101 <https://etherscan.io/address/0xB721Cc32160Ab0da2614CC6aB16eD822Aeebc101>`_

Factories
*********

.. csv-table::
   :header: "Name", "Source", "Address"

   StableSwap Factory, `FactorySidechains.vy <https://github.com/curvefi/curve-factory/blob/master/contracts/FactorySidechains.vy>`_, `0xD19Baeadc667Cf2015e395f2B08668Ef120f41F5 <https://blockscout.com/xdai/mainnet/address/0xD19Baeadc667Cf2015e395f2B08668Ef120f41F5>`_
   MetaUSD Zap, `MetaUSDZap.vy <https://blockscout.com/xdai/mainnet/address/0x87C067fAc25f123554a0E76596BF28cFa37fD5E9#code>`_, `0x87C067fAc25f123554a0E76596BF28cFa37fD5E9 <https://blockscout.com/xdai/mainnet/address/0x87C067fAc25f123554a0E76596BF28cFa37fD5E9>`_
   X-Chain Gauge Factory, `ChildGaugeFactory.vy <https://github.com/curvefi/curve-xchain-factory/blob/master/contracts/ChildGaugeFactory.vy>`_, `0xabC000d88f23Bb45525E447528DBF656A9D55bf5 <https://blockscout.com/xdai/mainnet/address/0xabC000d88f23Bb45525E447528DBF656A9D55bf5>`_


